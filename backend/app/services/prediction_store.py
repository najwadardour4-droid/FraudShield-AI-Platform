import json
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.prediction import AgentType, PredictionRecord


async def save_prediction(
    db: AsyncSession,
    *,
    agent_type: AgentType,
    user_email: str | None,
    input_summary: str,
    verdict: str,
    confidence: float,
    explanation: str,
    metadata: dict[str, Any] | None = None,
) -> PredictionRecord:
    record = PredictionRecord(
        agent_type=agent_type,
        user_email=user_email,
        input_summary=input_summary[:512],
        verdict=verdict,
        confidence=confidence,
        explanation=explanation,
        metadata_json=json.dumps(metadata or {}),
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record


async def list_predictions(
    db: AsyncSession,
    agent_type: AgentType | None = None,
    limit: int = 50,
) -> list[PredictionRecord]:
    stmt = select(PredictionRecord).order_by(PredictionRecord.created_at.desc()).limit(limit)
    if agent_type:
        stmt = stmt.where(PredictionRecord.agent_type == agent_type)
    result = await db.execute(stmt)
    return list(result.scalars().all())
