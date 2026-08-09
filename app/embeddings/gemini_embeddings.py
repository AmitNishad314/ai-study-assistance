import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import EMBEDDING_MODEL


load_dotenv()

api_key = settings.GEMINI_API_KEY

if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")


client = genai.Client(
    api_key=api_key
)

def create_document_embedding(text):

    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        )
    )

    return result.embeddings[0].values

def create_query_embedding(text):

    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )

    return result.embeddings[0].values

def embed_chunks(chunks):

    embedded_chunks = []


    for chunk in chunks:

        embedding = create_document_embedding(
            chunk["text"]
        )


        embedded_chunks.append({

            "id": chunk["id"],

            "text": chunk["text"],

            "metadata": chunk["metadata"],

            "embedding": embedding

        })


    return embedded_chunks