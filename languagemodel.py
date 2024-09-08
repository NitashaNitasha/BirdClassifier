import os
import google.generativeai as genai
from dotenv import load_dotenv

#loading env variables
load_dotenv()
API_KEY = os.getenv('API_KEY') or st.secrets['API_KEY']


# Set up API key
genai.configure(api_key=API_KEY)

def answer(question):
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

def RandomFact(bird):
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
