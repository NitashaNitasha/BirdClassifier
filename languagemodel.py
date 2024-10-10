import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key from Streamlit secrets or environment variables
try:
    API_KEY = st.secrets.get('API_KEY')
except FileNotFoundError:
    API_KEY = os.getenv('API_KEY')

# Set up API key
if not API_KEY:
    raise ValueError("API key not found. Please set it in Streamlit secrets or environment variables.")

genai.configure(api_key=API_KEY)

def answer(question):
    try:
        # Define generation configuration
        generation_config = {
            "temperature": 0.4,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        # Create the model
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",  # Ensure the model name is correct
            generation_config=generation_config,
            system_instruction="You are a bird information assistant. You only give information about birds asked. If the question is irrelevant, respond with 'I don't know.'",
        )

        # Start a chat session
        chat_session = model.start_chat()

        # Send a message and get the response
        response = chat_session.send_message(question)

        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error fetching response"

def RandomFact(bird):
    try:
        # Define generation configuration
        generation_config = {
            "temperature": 0.4,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        # Create the model
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",  # Ensure the model name is correct
            generation_config=generation_config,
            system_instruction="You are a bird information assistant. You can only give a random fact about bird asked. If you don't know don't answer, respond with 'I don't know.'.LIMIT the response to a 100 words.",
        )

        # Start a chat session
        chat_session = model.start_chat()

        # Send a message and get the response
        response = chat_session.send_message(bird)

        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error fetching response"
