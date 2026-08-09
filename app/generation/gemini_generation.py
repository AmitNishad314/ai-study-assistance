import os

from dotenv import load_dotenv

from google import genai

from config import MODEL_NAME


load_dotenv()


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

def generate_answer(prompt):

    response = client.models.generate_content(

        model=MODEL_NAME,

        contents=prompt

    )

    return response.text