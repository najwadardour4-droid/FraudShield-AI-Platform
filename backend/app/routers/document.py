from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user_email
from app.models.prediction import AgentType
from app.schemas.document import DocumentVerificationResponse
from app.services.document_service import document_service
from app.services.prediction_store import list_predictions, save_prediction

router = APIRouter(prefix="/document-verification", tags=["Alae — Document Verifier"])


@router.post("/verify", response_model=DocumentVerificationResponse)
async def verify_document(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    user_email: str | None = Depends(get_current_user_email),
):
    content = await file.read()
    result = document_service.predict(content, file.filename or "document.jpg")
    record = await save_prediction(
        db,
        agent_type=AgentType.DOCUMENT,
        user_email=user_email,
        input_summary=f"File: {file.filename}",
        verdict=result["verdict"],
        confidence=result["confidence"],
        explanation=result["explanation"],
        metadata=result["technical_details"],
    )
    return DocumentVerificationResponse(
        verdict=result["verdict"],
        confidence=result["confidence"],
        explanation=result["explanation"],
        anomalies=result.get("anomalies", []),
        technical_details=result.get("technical_details", {}),
        record_id=record.id,
    )


@router.get("/history")
async def document_history(limit: int = 50, db: AsyncSession = Depends(get_db)):
    rows = await list_predictions(db, AgentType.DOCUMENT, limit)
    return [
        {
            "id": r.id,
            "verdict": r.verdict,
            "confidence": r.confidence,
            "input_summary": r.input_summary,
            "explanation": r.explanation,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]
