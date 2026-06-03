import json
from typing import Any

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.prediction import AgentType, PredictionRecord


FLAGGED_VERDICTS = {"FRAUD", "PHISHING", "FAKE"}


async def get_analytics_summary(db: AsyncSession) -> dict[str, Any]:
    total_q = await db.execute(select(func.count()).select_from(PredictionRecord))
    total = total_q.scalar() or 0

    flagged_q = await db.execute(
        select(func.count()).select_from(PredictionRecord).where(PredictionRecord.verdict.in_(FLAGGED_VERDICTS))
    )
    flagged = flagged_q.scalar() or 0

    by_agent: list[dict[str, Any]] = []
    for agent in AgentType:
        if agent == AgentType.ORCHESTRATOR:
            continue
        count_q = await db.execute(
            select(func.count()).where(PredictionRecord.agent_type == agent)
        )
        agent_total = count_q.scalar() or 0
        flag_q = await db.execute(
            select(func.count())
            .where(PredictionRecord.agent_type == agent)
            .where(PredictionRecord.verdict.in_(FLAGGED_VERDICTS))
        )
        agent_flagged = flag_q.scalar() or 0
        avg_q = await db.execute(
            select(func.avg(PredictionRecord.confidence)).where(PredictionRecord.agent_type == agent)
        )
        avg_conf = float(avg_q.scalar() or 0)
        by_agent.append(
            {
                "agent": agent.value,
                "total": agent_total,
                "flagged": agent_flagged,
                "avg_confidence": round(avg_conf, 4),
            }
        )

    recent_q = await db.execute(
        select(PredictionRecord)
        .where(PredictionRecord.verdict.in_(FLAGGED_VERDICTS))
        .order_by(PredictionRecord.created_at.desc())
        .limit(10)
    )
    recent = [
        {
            "id": r.id,
            "agent": r.agent_type.value,
            "verdict": r.verdict,
            "confidence": r.confidence,
            "summary": r.input_summary,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in recent_q.scalars().all()
    ]

    return {
        "total_predictions": total,
        "total_flagged": flagged,
        "by_agent": by_agent,
        "recent_flagged": recent,
    }
