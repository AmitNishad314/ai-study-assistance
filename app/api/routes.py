from fastapi import APIRouter
from fastapi import UploadFile, File
import shutil
import os

from app.schemas.upload_response import UploadResponse
from app.services.ingestion_service import IngestionService

from app.services.rag_service import RAGService

router = APIRouter()
ingestion_service = IngestionService()

rag_service = RAGService()


@router.get("/")
def root():
    return {
        "message": "AI Document Assistant"
    }


@router.get("/chat")
def chat(question: str):

    answer = rag_service.ask(question)

    return {
        "answer": answer
    }
    
@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("storage/uploads", exist_ok=True)

    file_path = os.path.join(
        "storage/uploads",
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = ingestion_service.ingest(file_path)

    return UploadResponse(
        filename=file.filename,
        chunks=chunks,
        message="PDF indexed successfully."
    )