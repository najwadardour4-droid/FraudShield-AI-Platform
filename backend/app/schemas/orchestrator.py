from typing import Any

from pydantic import BaseModel, Field

from app.schemas.credit_card import CreditCardRequest


class OrchestratorRequest(BaseModel):
    run_credit_card: bool = False
    credit_card: CreditCardRequest | None = None
    run_phishing: bool = False
    phishing_text: str | None = None
    run_document: bool = False
    document_note: str | None = Field(default=None, description="Set when document uploaded via separate endpoint")


class OrchestratorResponse(BaseModel):
    summary: str
    highest_risk_agent: str | None
    results: list[dict[str, Any]]
