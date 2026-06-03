from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import AsyncSessionLocal, init_db
from app.routers import analytics, auth, credit_card, document, history, orchestrator, phishing
from app.services.auth_service import seed_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    async with AsyncSessionLocal() as db:
        await seed_users(db)
    yield


app = FastAPI(
    title="Multi-Agent AI Platform for Fraud & Scam Detection",
    description="PFE — Najwa (Credit Card) · Ferdaouss (Phishing) · Alae (Documents)",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prefix = settings.API_PREFIX
app.include_router(auth.router, prefix=prefix)
app.include_router(credit_card.router, prefix=prefix)
app.include_router(phishing.router, prefix=prefix)
app.include_router(document.router, prefix=prefix)
app.include_router(orchestrator.router, prefix=prefix)
app.include_router(analytics.router, prefix=prefix)
app.include_router(history.router, prefix=prefix)
app.include_router(websocket.router)


@app.get("/health")
async def health():
    return {"status": "ok", "agents": ["credit_card", "phishing", "document"]}
