import streamlit as st
from PIL import Image
import pytesseract
from gtts import gTTS
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import base64
from io import BytesIO

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash', google_api_key = api_key)

def encode_image_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


st.set_page_config(
    page_title="AI Vision Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown('''
    <style>
    .main {
        padding: 2rem;
    }
    .stSidebar {
        background-color: #2E4053;
        padding: 2rem;
        color: white !important;
    }
    .stSidebar h1, .stSidebar h2, .stSidebar h3 {
        color: white !important;
    }
    .stSidebar .stMarkdown {
        color: white !important;
    }
    .upload-section {
        border: 2px dashed #ccc;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
    }
    .stButton button {
        width: 100%;
        margin-top: 1rem;
    }
    </style>
''', unsafe_allow_html=True)


with st.sidebar:
    st.title("🔍 AI Vision Assistant")
    st.markdown("---")
    
    st.header("📋 About")
    st.write('''
    This AI-powered application assists visually impaired individuals by:
    
    - 🤖 Using Google's Generative AI for detailed scene descriptions
    - 📝 Converting text from images to speech
    - 🎯 Providing real-time visual assistance
    ''')
    
    st.markdown("---")
    st.header("🔧 Features")
    st.write('''
    1. Scene Understanding:
       - Detailed scene descriptions
       - Environment interpretation
       
    2. Text-to-Speech:
       - OCR text extraction
       - Natural voice synthesis
    ''')
    
    st.markdown("---")
    st.header("📝 How to Use")
    st.write('''
    1. Upload your image using the upload section
    2. Select your desired task (Scene Understanding or Text-to-Speech)
    3. Wait for AI processing
    4. Get detailed results!
    ''')
    
    st.markdown("---")
    st.header("ℹ️ Note")
    st.write('''
    This application uses:
    - Google's Generative AI (via LangChain)
    - OCR Technology
    - Text-to-Speech Synthesis
    ''')


col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("AI Vision Assistant")
    st.header("📤 Upload Image")
    
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        
        task = st.selectbox(
            "Select Task",
            ["Select a task", "Scene Understanding", "Text-to-Speech"],
            index=0,
            help="Choose the type of analysis you want to perform"
        )

        if task == "Scene Understanding":
            st.subheader("🎯 Scene Analysis")
            with st.spinner("Analyzing the scene using AI..."):
                try:
                    
                    base64_image = encode_image_to_base64(image)
                    
                    
                    prompt = ChatPromptTemplate.from_messages([
                        ("system", "You are an expert visual description assistant for visually impaired individuals."),
                        ("human", [
                            {"type": "text", "text": """
                            Provide a comprehensive and detailed description of this image. 
                            Focus on:
                            - Overall scene composition
                            - Key objects and their positions
                            - Colors, textures, and significant details
                            - Context and potential scenario
                            Describe the image as if you're helping a visually impaired person 
                            understand the scene completely and vividly.
                            Use descriptive language that paints a clear mental picture.
                            """},
                            {"type": "image_url", "image_url": f"data:image/png;base64,{base64_image}"}
                        ])
                    ])
                    
                    
                    output_parser = StrOutputParser()
                    
                    
                    chain = prompt | llm | output_parser
                    
                    
                    response = chain.invoke({})
                    
                    st.success("Analysis Complete!")
                    st.write(response)
                    
                except Exception as e:
                    st.error(f"Error in scene analysis: {str(e)}")

        elif task == "Text-to-Speech":
            st.subheader("📝 Text Extraction & Speech Conversion")
            with st.spinner("Processing image and converting to speech..."):
                try:
                    
                    extracted_text = pytesseract.image_to_string(image)
                    
                    if extracted_text.strip():
                        st.subheader("📄 Extracted Text")
                        st.write(extracted_text)
                        
                        
                        st.subheader("🔊 Audio Output")
                        tts = gTTS(text=extracted_text, lang='en')
                        tts.save("output.mp3")
                        st.audio("output.mp3", format="audio/mp3")
                        
                        
                        with open("output.mp3", "rb") as file:
                            st.download_button(
                                label="Download Audio",
                                data=file,
                                file_name="extracted_audio.mp3",
                                mime="audio/mp3"
                            )
                    else:
                        st.warning("No text detected in the image. Please try another image with clearer text.")
                except Exception as e:
                    st.error(f"Error in text extraction: {str(e)}")


st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>Built using Streamlit and LangChain's Google Generative AI</div>", 
    unsafe_allow_html=True
)