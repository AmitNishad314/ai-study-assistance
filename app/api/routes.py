import tempfile
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

from app.schemas.upload_response import UploadResponse
from app.services.ingestion_service import IngestionService
from app.services.rag_service import RAGService
from app.vector_store.chroma_store import ChromaStore
from app.embeddings.langchain_embeddings import EmbeddingService
from app.services.supabase_storage import SupabaseStorage
from app.utils.document_id import generate_document_id
from app.core.logging import logger

router = APIRouter()
embedding = EmbeddingService().get_embedding()
ingestion_service = IngestionService()
rag_service = RAGService()
vector_store = ChromaStore(embedding)
supabase_storage = SupabaseStorage()


@router.get("/")
def root():
    return {
        "message": "AI Document Assistant"
    }


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):
    result = rag_service.ask(request.question)
    return result


@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    filename = Path(file.filename or "uploaded.pdf").name
    document_id = generate_document_id()
    storage_path = supabase_storage.document_path(document_id)

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "upload.pdf"
        content = await file.read()
        file_path.write_bytes(content)

        try:
            supabase_storage.upload_pdf(storage_path, content)
            logger.info(f"Uploaded original PDF: {filename}")
            chunks = ingestion_service.ingest(
                str(file_path),
                filename,
                document_id,
                storage_path,
            )
        except Exception:
            try:
                vector_store.delete_document(document_id)
            except Exception:
                logger.exception("Failed to roll back indexed document")
            try:
                supabase_storage.delete_pdf(storage_path)
            except Exception:
                logger.exception("Failed to remove uploaded PDF after ingestion failure")
            raise

    logger.info(f"Indexed {chunks} chunks from {filename}")

    return UploadResponse(
        filename=filename,
        chunks=chunks,
        message="PDF indexed successfully."
    )


@router.get("/documents")
def documents():
    return vector_store.list_documents()


@router.delete("/documents/{document_id}")
def delete_document(document_id: str):
    try:
        vector_store.delete_document(document_id)
        supabase_storage.delete_pdf(
            supabase_storage.document_path(document_id)
        )
    except Exception as exc:
        logger.exception("Failed to delete document %s", document_id)
        raise HTTPException(
            status_code=502,
            detail="Document deletion failed in a storage service. Check backend logs and retry.",
        ) from exc

    return {
        "message": f"Document with ID {document_id} deleted successfully."
    }