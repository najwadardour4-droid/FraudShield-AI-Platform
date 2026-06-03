from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.analytics import AnalyticsSummary
from app.services.analytics_service import get_analytics_summary

router = APIRouter(prefix="/analytics", tags=["Dashboard Analytics"])


@router.get("/summary", response_model=AnalyticsSummary)
async def analytics_summary(db: AsyncSession = Depends(get_db)):
    data = await get_analytics_summary(db)
    return AnalyticsSummary(**data)
