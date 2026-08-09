from langchain_core.output_parsers import StrOutputParser

from app.embeddings.langchain_embeddings import EmbeddingService
from app.llm.langchain_llm import llm
from app.prompts.rag_prompt import rag_prompt
from app.vector_store.chroma_store import ChromaStore
from app.core.exceptions import APIException
from app.core.logging import logger


class RAGService:

    def __init__(self):

        embedding = EmbeddingService().get_embedding()

        self.vector_store = ChromaStore(embedding)

        self.parser = StrOutputParser()

    def ask(self, question):
        logger.info(f"Question: {question}")

        retriever = self.vector_store.as_retriever()
        

        docs = retriever.invoke(question)
        logger.info(f"Retrieved {len(docs)} chunks")

        context = ""

        sources = []

        for doc in docs:
    
          filename = doc.metadata.get(
            "filename",
            "Unknown"
        )
    
          page = doc.metadata.get(
            "page",
            0
        ) + 1
    
          context += f"""
        Document: {filename}
        Page: {page}
        
        {doc.page_content}
        
        ---------------------
        """
        
        sources.append({
                "filename": filename,
                "page": page
            })
    
        chain = rag_prompt | llm | self.parser
    
        try:
        
           answer = chain.invoke(
        
               {
                   "context": context,
                   "question": question
               }
        
           )
        
        except Exception as e:
        
           logger.exception(e)
           raise
        logger.info("Answer generated successfully.")
        return {
            "answer": answer,
            "sources": sources
        }