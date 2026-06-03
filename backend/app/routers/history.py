import json

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.prediction import AgentType
from app.services.prediction_store import list_predictions

router = APIRouter(prefix="/history", tags=["Prediction History"])


@router.get("")
async def unified_history(
    agent: str | None = Query(None, description="credit_card | phishing | document"),
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    agent_type = AgentType(agent) if agent else None
    rows = await list_predictions(db, agent_type, limit)
    return [
        {
            "id": r.id,
            "agent_type": r.agent_type.value,
            "verdict": r.verdict,
            "confidence": r.confidence,
            "input_summary": r.input_summary,
            "explanation": r.explanation,
            "metadata": json.loads(r.metadata_json or "{}"),
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]
