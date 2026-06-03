# 🛡️ AI-Powered Fraud Detection Platform (PFE)

An intelligent multi-agent platform that integrates **Machine Learning, Natural Language Processing, Computer Vision, and Large Language Models** to detect and investigate various types of fraud.

## 👥 Team Structure & Features

| Agent | Member | Technology | Feature Description |
|-------|--------|------------|---------------------|
| **Credit Card Investigator** | Najwa | XGBoost (99.96%) + SHAP | High-precision detection with 0-100 Risk Criticality scoring. |
| **Phishing Scanner** | Ferdaouss | NLP + LLM | Analyzes emails, messages, and URLs to identify phishing attempts. |
| **Document Verifier** | Alae | CNN (ResNet50) + Image Processing | Verifies document authenticity and detects potential forgeries. |

---

## 🚀 Platform Overview

The platform consists of three specialized AI agents working together:

1.  **Najwa (CreditCardInvestigator)**: An **Enterprise-Grade** system optimized for extreme class imbalance. Achieves **99.96% Accuracy** and **98.2% Precision**. It uses **SHAP (Explainable AI)** to highlight the top influencing features and provides a **0-100 Criticality Scale** for financial investigators.
2.  **Ferdaouss (PhishingScanner)**: Leverages NLP techniques to scan messages and URLs. It generates security recommendations and explains why a specific message is classified as a threat.
3.  **Alae (DocumentVerifier)**: Employs a CNN-based model (ResNet50) for image analysis. It can identify document types and flag visual anomalies indicative of tampering or forgery.

---

## 📂 Project Structure

```
fraud-detection-platform/
├── backend/                 # FastAPI + SQLite + AI Services
│   ├── app/
│   │   ├── routers/         # API Endpoints
│   │   ├── services/        # Business Logic & AI Integration
│   │   ├── models/          # Database Models (SQLAlchemy)
│   │   └── schemas/         # Data Validation (Pydantic)
│   ├── ai/                  # Training scripts & Alae's AI Pipeline
│   └── ml_models/           # Saved model artifacts (.pkl, .joblib, .pt)
├── frontend/                # Angular 21 (Modular Feature-based)
│   └── src/app/features/    # Dedicated modules for Najwa, Ferdaouss, and Alae
└── docs/                    # Detailed Architecture & Guides
```

## Prerequisites

- **Python 3.11+**
- **Node.js 20+** and npm
- (Optional) GPU for faster PyTorch — CPU works for demo

## Backend setup

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

# Train demo models (recommended)
python -m ai.train_credit_card
python -m ai.train_phishing

# Run API (from backend folder)
zzz
```

API docs: http://127.0.0.1:8000/docs

### Default login accounts

| Email | Password | Role |
|-------|----------|------|
| admin@fraudshield.ai | admin123 | admin |
| najwa@fraudshield.ai | agent123 | analyst |
| analyst@fraudshield.ai | analyst123 | analyst |

## Frontend setup

```bash
cd frontend
npm install
npm start
```

Open http://localhost:4200 — sign in with `admin@fraudshield.ai` / `admin123`.

## API endpoints (`/api/v1`)

| Method | Path | Agent |
|--------|------|-------|
| POST | `/auth/login` | Authentication |
| POST | `/credit-card-fraud/predict` | Najwa |
| POST | `/phishing-detection/scan` | Ferdaouss |
| POST | `/document-verification/verify` | Alae (multipart) |
| POST | `/orchestrator/analyze` | Multi-agent |
| GET | `/analytics/summary` | Dashboard KPIs |
| GET | `/history` | Unified audit log |

## Features

- Multi-agent modular architecture
- Explainable AI (SHAP, keyword signals, LLM-style narratives)
- SQLite prediction history
- JWT authentication
- SaaS-style responsive dashboard with analytics charts
- Separation: routers → services → models

## License

Academic use — PFE 2026.
