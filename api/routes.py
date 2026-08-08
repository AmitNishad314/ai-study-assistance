from fastapi import APIRouter, HTTPException
from fastapi import UploadFile, File
from pydantic import BaseModel, Field
from util.document_id import create_document_id
from rag_pipeline import answer_question
from vector_store.chroma_store import ChromaVectorStore
from embeddings.gemini_embeddings import embed_chunks

import os

from documents.pdf_reader import extract_pages,chunk_pages
from llm.gemini_client import generate_response

router = APIRouter()
store = ChromaVectorStore()

class Message(BaseModel):
    role: str
    text: str

class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=1000,
    )

    history: list[Message] = Field(default_factory=list)

class ChatResponse(BaseModel):
    response: str
    history: list[Message]


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:
        ans = answer_question(request.message, store)
        history = request.history.copy()
        
        history.append(Message(role="user", text=request.message))
        history.append(Message(role="assistant", text=ans))
        
        return {
            "response": ans,
            "history": history,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating response from LLM: {error}",
        ) from error


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        upload_dir = "storage/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        path = os.path.join("storage/uploads", file.filename)
        
        #save the uploaded file to disk
        with open(path, "wb") as pdf:
            pdf.write(await file.read())
            
        #extrach text page wise
        pages = extract_pages(path)
        #create one document id for the whole pdf
        document_id = create_document_id()
        #chunk pages
        chunks = chunk_pages(pages, file.filename,document_id)
        #generate emeddings for the chunks
        embedded_chunks = embed_chunks(chunks)
        #add chunks to the vector store
        store.add_chunks(embedded_chunks)
        
        total_characters = sum(len(page["text"]) for page in pages)
        
        return {
                "message": "PDF uploaded and processed successfully.",
                "filename": file.filename,
                "pages": len(pages),
                "characters": total_characters, 
                "chunks": len(chunks),
                "preview": (
                   chunks[0]["text"] if chunks else "No chunks generated"
                )
                }
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing PDF: {error}",
        ) from error

@router.get("/health")
def health_check():
    return {"status": "healthy"}