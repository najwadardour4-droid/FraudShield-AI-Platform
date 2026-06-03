# Fraud Detection Platform - Reorganized Structure

## Backend Structure (FastAPI)

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                   # FastAPI app entry point
│   │
│   ├── core/                     # Core configuration & utilities
│   │   ├── __init__.py
│   │   ├── config.py             # Environment variables, settings
│   │   ├── database.py           # SQLAlchemy setup
│   │   ├── deps.py               # FastAPI dependencies
│   │   └── security.py           # Authentication & authorization
│   │
│   ├── models/                   # SQLAlchemy database models
│   │   ├── __init__.py
│   │   ├── alert.py              # Alert model (if needed)
│   │   ├── prediction.py         # Prediction history model
│   │   └── user.py               # User model
│   │
│   ├── schemas/                  # Pydantic request/response models
│   │   ├── __init__.py
│   │   ├── credit_card.py        # Credit card schemas ← Najwa
│   │   ├── scam.py               # Phishing/scam schemas ← Ferdaouss
│   │   └── visual.py             # Document/visual schemas ← Alae
│   │
│   ├── routers/                  # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py               # Authentication routes
│   │   ├── credit_card.py        # Credit card endpoint ← Najwa
│   │   ├── scam.py               # Phishing endpoint ← Ferdaouss
│   │   └── visual.py             # Document endpoint ← Alae
│   │
│   └── services/                 # Business logic & ML model integration
│       ├── __init__.py
│       ├── credit_card_service.py # Credit card ML logic ← Najwa
│       ├── scam_service.py        # Phishing ML logic ← Ferdaouss
│       ├── visual_service.py      # Document ML logic ← Alae
│       └── prediction_store.py    # Store prediction history
│
├── ml_models/                    # Serialized ML models
│   ├── credit_card_model.pkl
│   ├── scam_model.pkl
│   └── visual_model.pkl
│
├── ai/                           # Model training scripts (if needed)
│   ├── __init__.py
│   ├── train_credit_card.py
│   ├── train_scam.py
│   └── train_visual.py
│
├── requirements.txt              # Python dependencies
├── run.ps1                        # Windows startup script
└── .env                          # Environment variables (gitignored)
```

## Frontend Structure (Angular)

```
frontend/src/app/
│
├── core/                         # Shared services, guards, interceptors
│   ├── guards/
│   │   └── auth.guard.ts        # Authentication & authorization
│   ├── interceptors/
│   │   └── http.interceptor.ts  # API call interceptor
│   ├── models/
│   │   └── fraud.models.ts      # Shared data models
│   └── services/
│       ├── api.service.ts        # Base API calls
│       └── auth.service.ts       # Authentication service
│
├── shared/                       # Reusable components & utilities
│   ├── components/
│   │   ├── particle-field/       # Visual effect component
│   │   ├── sidebar/              # Navigation sidebar
│   │   └── navbar/
│   └── prediction-result.component.ts  # Shared result display
│
├── features/                     # Feature modules (main structure)
│   │
│   ├── credit-card/              # Credit Card Fraud Detection ← Najwa
│   │   ├── components/
│   │   │   ├── card-investigator/     # Card analysis component
│   │   │   ├── score-ring/            # Risk score ring
│   │   │   └── inv-modal/             # Investigation modal
│   │   ├── services/
│   │   │   └── credit-card.service.ts # Feature service
│   │   ├── pages/
│   │   │   └── credit-card-agent/     # Main page
│   │   ├── credit-card.module.ts      # Feature module
│   │   ├── credit-card.routing.module.ts
│   │   └── index.ts
│   │
│   ├── scam/                     # Phishing/Scam Detection ← Ferdaouss
│   │   ├── components/
│   │   │   └── (phishing-specific components)
│   │   ├── services/
│   │   │   └── scam.service.ts
│   │   ├── pages/
│   │   │   └── scam-agent/
│   │   ├── scam.module.ts
│   │   ├── scam.routing.module.ts
│   │   └── index.ts
│   │
│   └── visual/                   # Document/Visual Fraud ← Alae
│       ├── components/
│       │   ├── grad-cam/             # Grad-CAM visualization
│       │   └── invoice-guard/        # Invoice analysis
│       ├── services/
│       │   └── visual.service.ts
│       ├── pages/
│       │   └── visual-agent/
│       ├── visual.module.ts
│       ├── visual.routing.module.ts
│       └── index.ts
│
├── layout/
│   └── shell.component.ts        # Main layout shell
│
├── app.ts                        # Root component
├── app.routes.ts                 # Main routing configuration
└── environments/
    └── environment.ts            # Environment config
```

## Development Workflow

### Each Developer's Workspace
- **Najwa**: Works on `backend/app/services/credit_card_service.py` and `frontend/src/app/features/credit-card/`
- **Ferdaouss**: Works on `backend/app/services/scam_service.py` and `frontend/src/app/features/scam/`
- **Alae**: Works on `backend/app/services/visual_service.py` and `frontend/src/app/features/visual/`

### Benefits of This Structure
1. **Clear Separation of Concerns**: Each feature is isolated and independent
2. **Scalability**: Easy to add new fraud detection types
3. **Team Collaboration**: Minimal merge conflicts with feature-based organization
4. **Maintainability**: Components, services, and routes are grouped logically
5. **Lazy Loading**: Features can be lazy-loaded for better performance

## Next Steps
1. Move existing components to appropriate feature directories
2. Update imports across the application
3. Update routing configuration
4. Remove old directory structures
5. Test all routes and functionality
