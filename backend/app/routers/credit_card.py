import json

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user_email
from app.models.prediction import AgentType
from app.schemas.credit_card import AgentPredictionResponse, CreditCardRequest
from app.services.credit_card_service import credit_card_service
from app.services.prediction_store import list_predictions, save_prediction

router = APIRouter(prefix="/credit-card-fraud", tags=["Najwa — Credit Card Fraud"])


@router.post("/predict", response_model=AgentPredictionResponse)
async def predict_credit_card_fraud(
    body: CreditCardRequest,
    db: AsyncSession = Depends(get_db),
    user_email: str | None = Depends(get_current_user_email),
):
    result = credit_card_service.predict(body.model_dump())
    record = await save_prediction(
        db,
        agent_type=AgentType.CREDIT_CARD,
        user_email=user_email,
        input_summary=f"Amount {body.amount} MAD, MCC {body.merchant_category}",
        verdict=result["verdict"],
        confidence=result["confidence"],
        explanation=result["explanation"],
        metadata=result["technical_details"],
    )
    return AgentPredictionResponse(**result, record_id=record.id)


@router.get("/history")
async def credit_card_history(limit: int = 50, db: AsyncSession = Depends(get_db)):
    rows = await list_predictions(db, AgentType.CREDIT_CARD, limit)
    return [
        {
            "id": r.id,
            "verdict": r.verdict,
            "confidence": r.confidence,
            "input_summary": r.input_summary,
            "explanation": r.explanation,
            "metadata": json.loads(r.metadata_json or "{}"),
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]
