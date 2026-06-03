from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user_email
from app.models.prediction import AgentType
from app.schemas.orchestrator import OrchestratorRequest, OrchestratorResponse
from app.services.orchestrator_service import orchestrator_service
from app.services.prediction_store import save_prediction

router = APIRouter(prefix="/orchestrator", tags=["Multi-Agent Orchestrator"])


@router.post("/analyze", response_model=OrchestratorResponse)
async def orchestrate(
    body: OrchestratorRequest,
    db: AsyncSession = Depends(get_db),
    user_email: str | None = Depends(get_current_user_email),
):
    cc_payload = body.credit_card.model_dump() if body.run_credit_card and body.credit_card else None
    phish_text = body.phishing_text if body.run_phishing else None

    outcome = orchestrator_service.analyze(
        credit_card_payload=cc_payload,
        phishing_text=phish_text,
    )

    await save_prediction(
        db,
        agent_type=AgentType.ORCHESTRATOR,
        user_email=user_email,
        input_summary="Multi-agent orchestration run",
        verdict="ALERT" if outcome["highest_risk_agent"] else "CLEAR",
        confidence=max((r["confidence"] for r in outcome["results"]), default=0.0),
        explanation=outcome["summary"],
        metadata={"results": outcome["results"]},
    )

    return OrchestratorResponse(**outcome)
