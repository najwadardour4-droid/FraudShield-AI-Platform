from pydantic import BaseModel


class AgentStats(BaseModel):
    agent: str
    total: int
    flagged: int
    avg_confidence: float


class AnalyticsSummary(BaseModel):
    total_predictions: int
    total_flagged: int
    by_agent: list[AgentStats]
    recent_flagged: list[dict]
