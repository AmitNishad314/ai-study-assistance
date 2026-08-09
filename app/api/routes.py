from fastapi import APIRouter

from app.services.rag_service import RAGService

router = APIRouter()

rag_service = RAGService()


@router.get("/")
def root():
    return {
        "message": "AI Document Assistant"
    }


@router.get("/chat")
def chat(question: str):

    answer = rag_service.ask(question)

    return {
        "answer": answer
    }