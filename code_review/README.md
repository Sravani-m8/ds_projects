
# AI Python Code Reviewer

This project leverages Google's Generative AI to build an AI-powered Python code reviewer that can analyze user-submitted Python code, suggest improvements, and answer coding-related queries.


## Project Overview

The **AI Python Code Reviewer** is a web application built using Streamlit that allows users to:

- Review their Python code for bugs and inefficiencies.
- Get suggestions for code improvements and fixed snippets.
- Ask coding-related questions and receive detailed explanations.

It leverages Google's **Generative AI** (Gemini model) to provide context-aware responses and code reviews.

Create a virtual environment and install the dependencies:



### Setup API Key

This project integrates with Google's generative AI, and you'll need a valid API key. Follow the steps below to get and set up your Google API key:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (if you haven't already).
3. Enable the **Gemini API** (or the relevant Google Generative AI service).
4. Generate an API key and copy it.

Create a `.env` file in the project root and add your API key:

```
GOOGLE_API_KEY=<your_google_api_key>
```


## How It Works

1. The user enters a Python code snippet or coding query in the text area provided in the application.
2. Once the user submits the query, the application sends the query to the **Google Generative AI** model.
3. The model processes the query and returns feedback on bugs, inefficiencies, or suggestions for improvement.
4. The user receives a detailed explanation or a corrected code snippet.

The AI acts as a professional Python code reviewer with a set of instructions to ensure relevant and high-quality responses.

### System Prompt

The AI model is configured with the following prompt:

```plaintext
You are a professional Python code reviewer. Your role is:
1. Review user-submitted Python code for bugs, inefficiencies, or errors.
2. Provide specific suggestions to improve the code and offer corrected code snippets where applicable.
3. Answer coding-related queries with detailed examples and explanations.
4. If the user asks questions outside the scope of coding, politely decline and request them to stick to coding topics.
```

## Features

- **Python Code Review**: Automatically analyze Python code for bugs, inefficiencies, and errors.
- **Suggestions and Fixes**: Get corrected code snippets with specific suggestions for improvement.
- **Coding Query Responses**: Ask coding-related questions and get detailed answers and examples.
- **Streamlit Interface**: User-friendly web interface built with Streamlit for an interactive experience.

## Usage

To use the AI Python Code Reviewer:

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Input your query**:
   - Paste a Python code snippet or ask a coding-related question in the text area.

3. **Generate the response**:
   - Click the **Generate Answer** button.
   - The AI will analyze your code or query and provide feedback below.

4. **View the response**:
   - The AI will display detailed suggestions, explanations, or corrected code.

