import streamlit as st
import google.generativeai as gen_ai 
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=api_key)


sys_prompt = """
You are a professional Python code reviewer. Your role is:
1. Review user-submitted Python code for bugs, inefficiencies, or errors.
2. Provide specific suggestions to improve the code and offer corrected code snippets where applicable.
3. Answer coding-related queries with detailed examples and explanations.
4. If the user asks questions outside the scope of coding, politely decline and request them to stick to coding topics.
"""


model = gen_ai.GenerativeModel(
    model_name="models/gemini-1.5-flash", 
    system_instruction=sys_prompt
)


st.set_page_config(
    page_title="AI Python Code Reviewer",
    layout="wide",
)


st.markdown(
    """
    <style>
        /* Style the app title in yellow */
        .app-title {
            color: yellow;
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
        }

        /* Center align the text input box */
        .stTextArea {
            margin: 0 auto;
        }

        /* Sidebar background and styling */
        .css-1d391kg {
            background-color: #f0f8ff;
            border-right: 2px solid #d0d0d0;
        }

        /* Set the background color of the main app */
        body {
            background-color: #f5f5f5;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.sidebar.title("Welcome")
st.sidebar.markdown(
    """
    **This application will help you:**
    - Review your Python code for bugs and inefficiencies.
    - Receive fixed code snippets with suggestions.
    - Answer coding-related questions with detailed explanations.

    **Steps to Use:**
    1. Enter your Python code or coding query in the box.
    2. Click the **Generate Answer** button.
    3. View the response below.

    """
)


st.markdown('<div class="app-title">AI Python Code Reviewer Application</div>', unsafe_allow_html=True)


user_prompt = st.text_area(
    "Enter your coding query:",
    placeholder="Paste your coding question here...",
    height=300,
)


btn_click = st.button("Generate Answer")


if btn_click and user_prompt.strip():
    try:
        response = model.generate_content(user_prompt)
        st.subheader("Response for your query:")
        st.write(response.text)

    except Exception as e:
        st.error(f"An error occurred: {e}")
elif btn_click:
    st.warning("Please enter your Python code or coding query before clicking 'Generate Answer'.")
