from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user_email
from app.models.prediction import AgentType
from app.schemas.credit_card import AgentPredictionResponse
from app.schemas.phishing import PhishingScanRequest
from app.services.phishing_service import phishing_service
from app.services.prediction_store import list_predictions, save_prediction

router = APIRouter(prefix="/phishing-detection", tags=["Ferdaouss — Phishing Scanner"])


@router.post("/scan", response_model=AgentPredictionResponse)
async def scan_phishing(
    body: PhishingScanRequest,
    db: AsyncSession = Depends(get_db),
    user_email: str | None = Depends(get_current_user_email),
):
    result = phishing_service.predict(body.text, body.channel)
    record = await save_prediction(
        db,
        agent_type=AgentType.PHISHING,
        user_email=user_email,
        input_summary=body.text[:200] + ("..." if len(body.text) > 200 else ""),
        verdict=result["verdict"],
        confidence=result["confidence"],
        explanation=result["explanation"],
        metadata=result["technical_details"],
    )
    return AgentPredictionResponse(**result, record_id=record.id)


@router.get("/history")
async def phishing_history(limit: int = 50, db: AsyncSession = Depends(get_db)):
    rows = await list_predictions(db, AgentType.PHISHING, limit)
    return [
        {
            "id": r.id,
            "verdict": r.verdict,
            "confidence": r.confidence,
            "input_summary": r.input_summary,
            "explanation": r.explanation,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]
