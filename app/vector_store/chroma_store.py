from langchain_chroma import Chroma
import uuid
from app.core.config import settings


class ChromaStore:

    def __init__(self, embedding_function):

        self.db = Chroma(
            persist_directory=settings.CHROMA_DIR,
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

     return self.db.as_retriever(
    search_kwargs={
        "k": 5
    }
    )
     
    def list_documents(self):
        
        result = self.db.get()
        docs = {}

        for metadata in result["metadatas"]:
            document_id = metadata.get("document_id")
            filename = metadata.get("filename")

            if document_id not in docs:
                docs[document_id] = {
                    "filename": filename,
                    "pages": [],
                    "chunks":0
                }

            docs[document_id]["chunks"]+=1
        return docs
    
    def delete_document(self, document_id):
        
        result = self.db.get(
            where={
                "document_id" :document_id 
                }
        )
