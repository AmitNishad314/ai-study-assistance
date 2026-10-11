import chromadb
from langchain_chroma import Chroma

from app.core.config import settings


class ChromaStore:

    def __init__(self, embedding_function):
        client = chromadb.CloudClient(
            api_key=settings.CHROMA_API_KEY,
            tenant=settings.CHROMA_TENANT,
            database=settings.CHROMA_DATABASE,
        )
        self.db = Chroma(
            client=client,
            collection_name="mentorai_documents",
            embedding_function=embedding_function,
        )

    def add_documents(self, documents):

        ids = []
    
        for i, doc in enumerate(documents):
    
            document_id = doc.metadata["document_id"]
    
            ids.append(
                f"{document_id}_{i}"
            )
    
        self.db.add_documents(
            documents,
            ids=ids
        )

    def as_retriever(self):
        return self.db.as_retriever(search_kwargs={"k": 5})

    def list_documents(self):
        result = self.db.get()
        docs = {}

        for metadata in result.get("metadatas") or []:
            if not metadata:
                continue
            document_id = metadata.get("document_id")
            if not document_id:
                continue

            filename = metadata.get("filename")

            if document_id not in docs:
                docs[document_id] = {
                    "document_id": document_id,
                    "filename": filename,
                    "chunks": 0,
                    "ingested_at": metadata.get("ingested_at"),
                }

            docs[document_id]["chunks"] += 1

        return list(docs.values())

    def delete_document(self, document_id):
        self.db.delete(where={"document_id": document_id})
