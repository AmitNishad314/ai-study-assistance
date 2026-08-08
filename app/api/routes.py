from fastapi import APIRouter

from app.services.chat_service import ChatService

router = APIRouter()

service = ChatService()


@router.get("/")
def root():
    return {"message": "AI Document Assistant"}


@router.get("/chat")
def chat(question: str):

    answer = service.ask(question)

    return {
        "answer": answer
    }