from typing import Any
from pydantic import BaseModel, Field


class DocumentVerificationResponse(BaseModel):
    agent: str = "document_verifier"
    verdict: str
    confidence: float
    explanation: str
    anomalies: list[str] = []
    technical_details: dict[str, Any] = Field(default_factory=dict)
    record_id: int | None = None
