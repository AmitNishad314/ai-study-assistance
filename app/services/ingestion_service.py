from datetime import datetime, timezone

from app.documents.pdf_loader import PDFLoader
from app.documents.text_splitter import DocumentSplitter
from app.embeddings.langchain_embeddings import EmbeddingService
from app.vector_store.chroma_store import ChromaStore
from app.core.logging import logger


class IngestionService:

    def ingest(self, pdf_path, filename, document_id, storage_path):
        loader = PDFLoader()
        splitter = DocumentSplitter()
        embedding_service = EmbeddingService()

        docs = loader.load(pdf_path)
        chunks = splitter.split(docs)

        ingested_at = datetime.now(timezone.utc).isoformat()
        for chunk in chunks:
            page = chunk.metadata.get("page")
            chunk.metadata = {
                "page": page if isinstance(page, int) else 0,
                "document_id": document_id,
                "filename": filename,
                "storage_path": storage_path,
                "ingested_at": ingested_at,
            }

        vector_store = ChromaStore(
            embedding_service.get_embedding()
        )
        vector_store.add_documents(chunks)

        logger.info(f"Indexed {len(chunks)} chunks successfully.")
        return len(chunks)