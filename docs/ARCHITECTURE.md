# 🏗️ AI-Powered Fraud Detection Platform Architecture

## Overview

The platform is designed as a **Multi-Agent AI ecosystem** where specialized agents (Najwa, Ferdaouss, Alae) handle different fraud domains. A central FastAPI backend coordinates these agents, while a modern Angular frontend provides a unified dashboard for analysts.

## 🤖 Specialized AI Agents

| Agent | Owner | Model Architecture | Input Data | Output / Insights |
|-------|-------|-------|-------|--------|
| **Credit Card Investigator** | Najwa | XGBoost + SHAP | Transaction Features | Risk score, top fraud drivers, LLM explanation |
| **Phishing Scanner** | Ferdaouss | NLP (TF-IDF + LogReg) | Email/SMS/URL | Phishing probability, threat signals, security tips |
| **Document Verifier** | Alae | **ResNet50 (CNN)** | Image Upload | Authenticity score, OCR metadata, visual anomalies |

## 🛠️ Technical Stack

- **Backend**: FastAPI (Python 3.11+), SQLAlchemy (SQLite), PyTorch (CNN), XGBoost (ML).
- **Frontend**: Angular 21, Lucide Icons, Feature-based modularity.
- **AI Integration**: Custom AI pipelines in `backend/ai/` and model artifacts in `backend/ml_models/`.

```
┌─────────────────────────────────────────────────────────┐
│  Angular 21 SPA — dashboard, 3 modules, auth, charts    │
└──────────────────────────┬──────────────────────────────┘
                           │ REST / JSON / multipart
┌──────────────────────────▼──────────────────────────────┐
│  FastAPI — routers (controllers) → services → AI layer    │
│  Orchestrator — asyncio.gather on selected agents         │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│  SQLite — users, prediction_history (audit trail)         │
│  ml_models/ — .pkl, .joblib, .pt artifacts                │
└─────────────────────────────────────────────────────────┘
```

## API Routes (`/api/v1`)

- `POST /auth/login` — mock JWT auth
- `POST /credit-card-fraud/predict` — Najwa
- `GET /credit-card-fraud/history`
- `POST /phishing-detection/scan` — Ferdaouss
- `GET /phishing-detection/history`
- `POST /document-verification/verify` — Alae (multipart)
- `GET /document-verification/history`
- `POST /orchestrator/analyze` — multi-agent run
- `GET /analytics/summary` — dashboard KPIs

## Frontend Routes

- `/login` — authentication UI
- `/dashboard` — KPIs + charts
- `/agents/credit-card` — transaction form
- `/agents/phishing` — text scanner
- `/agents/document` — image upload
- `/history` — unified prediction log
