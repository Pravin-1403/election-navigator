from fastapi import APIRouter, HTTPException
import logging
from models.models import ChatRequest, ChatResponse
from services.ai_service import generate_election_response

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/ask", response_model=ChatResponse)
async def ask_question(request: ChatRequest):
    logger.info(f"Received query: {request.query}")
    try:
        user_context = request.user_info.model_dump() if request.user_info else {}
        history_dicts = [msg.model_dump() for msg in request.history] if request.history else []
        answer = generate_election_response(request.query, user_context, history_dicts)
        return ChatResponse(response=answer)
    except RuntimeError as e:
        logger.error(f"AI Service Error: {e}")
        raise HTTPException(status_code=502, detail="Failed to connect to AI Service")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An internal server error occurred")
