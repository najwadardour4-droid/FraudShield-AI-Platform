import enum

from sqlalchemy import Column, DateTime, Enum, Float, Integer, String, Text
from sqlalchemy.sql import func

from app.core.database import Base


class AgentType(str, enum.Enum):
    CREDIT_CARD = "credit_card"
    PHISHING = "phishing"
    DOCUMENT = "document"
    ORCHESTRATOR = "orchestrator"


class PredictionRecord(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)
    agent_type = Column(Enum(AgentType), nullable=False, index=True)
    user_email = Column(String, nullable=True)
    input_summary = Column(String(512))
    verdict = Column(String(32), nullable=False)  # FRAUD | PHISHING | FAKE | SAFE | LEGITIMATE
    confidence = Column(Float, nullable=False)
    explanation = Column(Text)
    metadata_json = Column(Text)  # JSON: SHAP, keywords, CNN scores, etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
