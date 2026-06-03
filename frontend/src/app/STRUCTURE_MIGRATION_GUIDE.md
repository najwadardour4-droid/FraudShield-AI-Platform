# Angular Structure Reorganization

## New Structure Overview

```
frontend/src/app/
├── core/                          # Shared configuration, auth, guards, interceptors
│   ├── guards/
│   │   └── auth.guard.ts
│   ├── interceptors/
│   ├── models/
│   │   └── fraud.models.ts
│   └── services/
│       ├── api.service.ts
│       └── auth.service.ts
│
├── shared/                        # Reusable components and utilities
│   ├── components/
│   │   ├── particle-field/
│   │   └── sidebar/
│   └── prediction-result.component.ts
│
├── features/                      # Feature modules
│   ├── credit-card/               # Credit Card Fraud Detection (Najwa)
│   │   ├── components/
│   │   │   ├── card-investigator/
│   │   │   ├── score-ring/
│   │   │   └── inv-modal/
│   │   ├── services/
│   │   │   └── credit-card.service.ts
│   │   ├── pages/
│   │   │   └── credit-card-agent/
│   │   ├── credit-card.module.ts
│   │   ├── credit-card.routing.module.ts
│   │   └── index.ts
│   │
│   ├── scam/                      # Phishing/Scam Detection (Ferdaouss)
│   │   ├── components/
│   │   ├── services/
│   │   │   └── scam.service.ts
│   │   ├── pages/
│   │   │   └── scam-agent/
│   │   ├── scam.module.ts
│   │   ├── scam.routing.module.ts
│   │   └── index.ts
│   │
│   └── visual/                    # Document/Visual Fraud Detection (Alae)
│       ├── components/
│       │   ├── grad-cam/
│       │   └── invoice-guard/
│       ├── services/
│       │   └── visual.service.ts
│       ├── pages/
│       │   └── visual-agent/
│       ├── visual.module.ts
│       ├── visual.routing.module.ts
│       └── index.ts
│
├── layout/                        # Main layout/shell
│   └── shell.component.ts
│
├── app.ts                         # Root component
├── app.routes.ts                  # Updated routing (needs modification)
└── ...
```

## Next Steps

### 1. Move Existing Components
Move components from old locations to feature modules:
- `components/card-investigator/` → `features/credit-card/components/`
- `components/score-ring/` → `features/credit-card/components/`
- `components/inv-modal/` → `features/credit-card/components/`
- `components/grad-cam/` → `features/visual/components/`
- `components/invoice-guard/` → `features/visual/components/`
- `components/particle-field/` → `shared/components/`
- `components/sidebar/` → `shared/components/`

### 2. Move Services
Move service files to appropriate feature modules:
- Create feature-specific services in each `features/*/services/` directory
- Move general services to `core/services/` (api.service.ts, auth.service.ts)

### 3. Update Routes
Update `app.routes.ts` to use the new feature module structure:
```typescript
{
  path: 'agents',
  children: [
    { path: 'credit-card', loadChildren: () => import('./features/credit-card/credit-card.module').then(m => m.CreditCardModule) },
    { path: 'phishing', loadChildren: () => import('./features/scam/scam.module').then(m => m.ScamModule) },
    { path: 'document', loadChildren: () => import('./features/visual/visual.module').then(m => m.VisualModule) },
  ]
}
```

### 4. Update Imports
Update all component imports across the application to reference the new locations.

### 5. Remove Old Directories
Once all files have been moved and imports updated:
- Delete `pages/agents/` (content moved to features)
- Delete `components/` (content distributed to features and shared)
- Keep `pages/` for auth pages if needed

## Assignment Structure

- **Najwa**: `features/credit-card/` - Credit card fraud detection module
- **Ferdaouss**: `features/scam/` - Phishing/scam fraud detection module  
- **Alae**: `features/visual/` - Document/invoice fraud detection module

Each developer can work independently on their feature module without conflicts.
