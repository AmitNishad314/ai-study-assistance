from langchain_chroma import Chroma
import uuid


class ChromaStore:

    def __init__(self, embedding_function):

        self.db = Chroma(
            persist_directory="storage/chroma_db",
            embedding_function=embedding_function,
        )

    def add_documents(self, documents):

       ids = [
           str(uuid.uuid4())
           for _ in documents
       ]
   
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