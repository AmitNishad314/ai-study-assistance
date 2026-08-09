from fastapi import APIRouter
from fastapi import UploadFile, File
import shutil
import os

from app.schemas.upload_response import UploadResponse
from app.services.ingestion_service import IngestionService

from app.services.rag_service import RAGService
from app.vector_store.chroma_store import ChromaStore
from app.embeddings.langchain_embeddings import EmbeddingService
from app.services.document_registry import DocumentRegistry


router = APIRouter()
embedding = EmbeddingService().get_embedding()
ingestion_service = IngestionService()
rag_service = RAGService()
vector_store = ChromaStore(embedding)
registry = DocumentRegistry()


@router.get("/")
def root():
    return {
        "message": "AI Document Assistant"
    }


from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    result = rag_service.ask(request.question)

    return result
    
@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("storage/uploads", exist_ok=True)

    file_path = os.path.join(
        "storage/uploads",
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = ingestion_service.ingest(file_path,file.filename)

    return UploadResponse(
        filename=file.filename,
        chunks=chunks,
        message="PDF indexed successfully."
    )
    
@router.get("/documents")
def documents():
    return registry.list_documents()


@router.delete("/documents/{document_id}")
def delete_document(document_id: str):
    vector_store.delete_document(document_id)
    registry.delete_document(document_id)
    return {
        "message": f"Document with ID {document_id} deleted successfully."
    }