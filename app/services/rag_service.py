from langchain_core.output_parsers import StrOutputParser

from app.embeddings.langchain_embeddings import EmbeddingService
from app.llm.langchain_llm import llm
from app.prompts.rag_prompt import rag_prompt
from app.vector_store.chroma_store import ChromaStore


class RAGService:

    def __init__(self):

        embedding = EmbeddingService().get_embedding()

        self.vector_store = ChromaStore(embedding)

        self.parser = StrOutputParser()

    def ask(self, question):

        retriever = self.vector_store.as_retriever()

        docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        chain = rag_prompt | llm | self.parser

        return chain.invoke(
            {
                "context": context,
                "question": question
            }
        )