from app.documents.pdf_loader import PDFLoader
from app.documents.text_splitter import DocumentSplitter
from app.embeddings.langchain_embeddings import EmbeddingService
from app.vector_store.chroma_store import ChromaStore


class IngestionService:

    def ingest(self, pdf_path):

        loader = PDFLoader()

        splitter = DocumentSplitter()

        embedding_service = EmbeddingService()

        docs = loader.load(pdf_path)

        chunks = splitter.split(docs)
        
        import os

        from app.utils.document_id import generate_document_id

        document_id = generate_document_id(filename)
        
        for chunk in chunks:
            chunk.metadata["document_id"] = document_id
            chunk.metadata["filename"] = filename
        
        vector_store = ChromaStore(
            embedding_service.get_embedding()
        )

        vector_store.add_documents(chunks)

        print(f"Indexed {len(chunks)} chunks successfully.")