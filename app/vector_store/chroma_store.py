from langchain_chroma import Chroma


class ChromaStore:

    def __init__(self, embedding_function):

        self.db = Chroma(
            persist_directory="storage/chroma_db",
            embedding_function=embedding_function,
        )

    def add_documents(self, documents):
        self.db.add_documents(documents)

    def as_retriever(self):

     return self.db.as_retriever(
        search_kwargs={
            "k": 4
        }
    )