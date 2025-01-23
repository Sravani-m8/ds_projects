
# AI Vision Assistant

The **AI Vision Assistant** is an AI-powered application designed to assist visually impaired individuals by providing two key functionalities:

1. **Scene Understanding**: Generate detailed descriptions of images, including scene composition and context.
2. **Text-to-Speech**: Convert text from images into speech using Optical Character Recognition (OCR) technology and Google’s Text-to-Speech synthesis.




## Installation

### Install the required libraries

Create a virtual environment and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

pip install -r requirements.txt
```

###  Setup API Key

This project uses **Google's Generative AI** via LangChain and requires an API key. To set it up:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (if needed).
3. Enable the **Google Generative AI API**.
4. Create an API key and copy it.

Add the following line to your `.env` file:

```
GOOGLE_API_KEY=<your_google_api_key>
```




## Project Overview

The **AI Vision Assistant** is a web application built with Streamlit that helps visually impaired users by providing two main features:

1. **Scene Understanding**: Generate descriptive analyses of images.
2. **Text-to-Speech**: Convert the text in images into speech.

The application uses **Google's Generative AI**, **OCR technology**, and **Text-to-Speech synthesis** to perform these tasks in real-time.

## Features

- **Scene Understanding**: Analyze and describe images, including objects, composition, and context. Ideal for providing scene descriptions to visually impaired users.
  
- **Text-to-Speech**: Extract and read text from images using OCR. The extracted text is then converted into speech with Google’s Text-to-Speech API.

## Usage

### 1. Run the Streamlit app

To run the application locally:

```bash
streamlit run app.py
```

### 2. Upload Image

Once the application is running:

1. **Upload an image** via the upload section.
2. **Choose a task**:
   - **Scene Understanding**: Generate a detailed description of the scene in the image.
   - **Text-to-Speech**: Convert any text found in the image into speech.

### 3. View the results

- For **Scene Understanding**, the AI will process the image and provide a detailed description of the scene.
- For **Text-to-Speech**, the extracted text will be shown, and you can listen to it by clicking on the audio player.

### 4. Download Audio

For the Text-to-Speech feature, you can download the generated audio file by clicking the **Download Audio** button.


## Technologies

This project uses the following technologies:

- **Streamlit**: For building the web application interface.
- **Google Generative AI**: For generating scene descriptions (via LangChain's ChatGoogleGenerativeAI).
- **pytesseract**: For Optical Character Recognition (OCR) to extract text from images.
- **gTTS (Google Text-to-Speech)**: To convert extracted text into speech.
- **LangChain**: To integrate Google’s Generative AI with the application.

