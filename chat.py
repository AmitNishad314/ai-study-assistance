from rag_pipeline import answer_question
from vector_store.faiss_store import FaissVectorStore
from vector_store.chroma_store import ChromaVectorStore

store = ChromaVectorStore()


print("RAG Ready!")

while True:
    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    answer = answer_question(question, store)

    print("\nAnswer:")
    print(answer)