from typing import Any

from pydantic import BaseModel, Field


class CreditCardRequest(BaseModel):
    amount: float = Field(..., gt=0, examples=[1250.50])
    merchant_category: str = Field(..., examples=["online_retail"])
    hour_of_day: int = Field(..., ge=0, le=23, examples=[3])
    distance_from_home_km: float = Field(..., ge=0, examples=[420.0])
    v1: float = 0.0
    v2: float = 0.0
    v3: float = 0.0


class AgentPredictionResponse(BaseModel):
    agent: str
    verdict: str
    confidence: float
    explanation: str
    technical_details: dict[str, Any] = Field(default_factory=dict)
    record_id: int | None = None
