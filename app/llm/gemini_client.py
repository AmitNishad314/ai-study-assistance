import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MODEL_NAME, SYSTEM_PROMPT


load_dotenv(".env")


def _get_client():
    api_key = settings.GEMINI_API_KEY

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Add it to your .env file."
        )

    return genai.Client(api_key=api_key)


def generate_response(user_message, history=None):
    """
    Generate a Gemini response while maintaining conversation history.

    history format:
    [
        {"role": "user", "text": "..."},
        {"role": "model", "text": "..."}
    ]
    """

    if history is None:
        history = []

    client = _get_client()

    contents = []

    # Add previous conversation
    for message in history:
        contents.append(
            types.Content(
                role=message["role"],
                parts=[
                    types.Part.from_text(
                        text=message["text"]
                    )
                ],
            )
        )

    # Add current user message
    contents.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=user_message
                )
            ],
        )
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT.strip()
        ),
    )

    response_text = response.text

    # Update conversation history
    updated_history = history + [
        {
            "role": "user",
            "text": user_message,
        },
        {
            "role": "model",
            "text": response_text,
        },
    ]

    return {
        "response": response_text,
        "history": updated_history,
    }


def stream_response(user_message, history=None):
    """
    Streaming version used by the CLI.
    """

    if history is None:
        history = []

    client = _get_client()

    contents = []

    for message in history:
        contents.append(
            types.Content(
                role=message["role"],
                parts=[
                    types.Part.from_text(
                        text=message["text"]
                    )
                ],
            )
        )

    contents.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=user_message
                )
            ],
        )
    )

    full_response = ""

    stream = client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT.strip()
        ),
    )

    for chunk in stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text

    print()

    updated_history = history + [
        {
            "role": "user",
            "text": user_message,
        },
        {
            "role": "model",
            "text": full_response,
        },
    ]

    return updated_history