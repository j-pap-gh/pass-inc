
from fastapi import APIRouter
from app.schemas.ai import ChatRequest
from app.services.ai_service import AIService

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    return AIService().chat(req.message)
