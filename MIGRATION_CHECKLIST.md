# Migration Checklist - Angular Frontend Restructuring

## ✅ Completed Scaffolding

The following structure has been created:

### Directory Structure Created
- ✅ `frontend/src/app/features/credit-card/` with `components/`, `services/`, `pages/`
- ✅ `frontend/src/app/features/scam/` with `components/`, `services/`, `pages/`
- ✅ `frontend/src/app/features/visual/` with `components/`, `services/`, `pages/`

### Files Created
- ✅ Feature modules (`*.module.ts` and `*.routing.module.ts` for each feature)
- ✅ Feature services (`credit-card.service.ts`, `scam.service.ts`, `visual.service.ts`)
- ✅ Placeholder page components
- ✅ Index files for better module exports

### Documentation Created
- ✅ `STRUCTURE_MIGRATION_GUIDE.md` - Step-by-step migration guide
- ✅ `RESTRUCTURE_GUIDE.md` - Complete restructuring overview

---

## 📋 TODO: Component Migration

### Credit Card Module (Najwa)
Assign to: **Najwa**
- [ ] Move `components/card-investigator/` → `features/credit-card/components/`
- [ ] Move `components/score-ring/` → `features/credit-card/components/`
- [ ] Move `components/inv-modal/` → `features/credit-card/components/`
- [ ] Update all imports in these components
- [ ] Replace placeholder `credit-card-agent.component.ts` with actual content from `pages/agents/credit-card/`
- [ ] Move `services/fraud-api.service.ts` methods to `credit-card.service.ts` (credit card specific)
- [ ] Update routing module to point to new component locations

### Scam/Phishing Module (Ferdaouss)
Assign to: **Ferdaouss**
- [ ] Create phishing-specific components in `features/scam/components/`
- [ ] Replace placeholder `scam-agent.component.ts` with actual content from `pages/agents/phishing/`
- [ ] Move phishing-related services to `scam.service.ts`
- [ ] Update routing module for scam feature

### Visual/Document Module (Alae)
Assign to: **Alae**
- [ ] Move `components/grad-cam/` → `features/visual/components/`
- [ ] Move `components/invoice-guard/` → `features/visual/components/`
- [ ] Replace placeholder `visual-agent.component.ts` with actual content from `pages/agents/document/`
- [ ] Move document-related services to `visual.service.ts`
- [ ] Update routing module for visual feature

---

## 📋 TODO: Shared Components & Services

### Shared Components
- [ ] Move `components/particle-field/` → `shared/components/`
- [ ] Move `components/sidebar/` → `shared/components/`
- [ ] Create `shared/components/index.ts` for exports
- [ ] Keep `shared/prediction-result.component.ts` and ensure it's accessible to all features

### Core Services
- [ ] Keep base services in `core/services/`:
  - [ ] `api.service.ts` - Base HTTP service
  - [ ] `auth.service.ts` - Authentication
- [ ] Move feature-specific service logic to respective features

### Core Models & Guards
- [ ] Ensure `core/models/fraud.models.ts` has all shared interfaces
- [ ] Update `core/guards/auth.guard.ts` if needed
- [ ] Organize `core/interceptors/` for API calls

---

## 📋 TODO: Routing Configuration

### Update app.routes.ts
- [ ] Import feature modules
- [ ] Update routes for new structure:
  ```typescript
  {
    path: 'agents',
    canActivate: [authGuard],
    children: [
      { path: 'credit-card', loadComponent: () => import('./features/credit-card/pages/credit-card-agent/credit-card-agent.component').then(m => m.CreditCardAgentComponent) },
      { path: 'phishing', loadComponent: () => import('./features/scam/pages/scam-agent/scam-agent.component').then(m => m.ScamAgentComponent) },
      { path: 'document', loadComponent: () => import('./features/visual/pages/visual-agent/visual-agent.component').then(m => m.VisualAgentComponent) },
    ]
  }
  ```

### Update dashboard & other pages
- [ ] Update imports in `pages/dashboard/` to reference new feature paths
- [ ] Update any navigation links to new routes
- [ ] Test all navigation between features

---

## 📋 TODO: Import Updates

- [ ] Search and replace all old import paths in the codebase:
  - [ ] `from './pages/agents/` → `from './features/[feature]/pages/`
  - [ ] `from './components/` → `from './features/[feature]/components/` or `from './shared/components/`
  - [ ] `from './services/` → Review and update to appropriate location

- [ ] Use VS Code Find & Replace (Ctrl+H) for bulk updates:
  ```
  Old:     './pages/agents/credit-card/'
  New:     './features/credit-card/pages/credit-card-agent/'
  
  Old:     './pages/agents/phishing/'
  New:     './features/scam/pages/scam-agent/'
  
  Old:     './pages/agents/document/'
  New:     './features/visual/pages/visual-agent/'
  
  Old:     './components/card-investigator/'
  New:     './features/credit-card/components/card-investigator/'
  
  Old:     './components/score-ring/'
  New:     './features/credit-card/components/score-ring/'
  ```

---

## 📋 TODO: Cleanup

### After All Files Are Moved & Imports Updated
- [ ] Delete `pages/agents/` directory (content moved to features)
- [ ] Delete old `components/` directory (content distributed)
- [ ] Delete `pages/` directory if only agents remain (or keep if login page is there)
- [ ] Verify no broken imports remain

### Testing
- [ ] `ng serve` and verify app loads without errors
- [ ] Test all routes: `/agents/credit-card`, `/agents/phishing`, `/agents/document`
- [ ] Test authentication and navigation
- [ ] Verify all components render correctly
- [ ] Check browser console for import errors

---

## 📋 TODO: Backend Reorganization (Optional)

### Rename endpoints for clarity
If you also want to reorganize the backend routers:
- [ ] Rename `credit_card.py` → keep as is (already clear)
- [ ] Rename `phishing.py` → `scam.py` (for consistency with frontend)
- [ ] Update FastAPI router registrations in `main.py`
- [ ] Update request/response schemas similarly

---

## 🎯 Quick Reference: Who Does What?

| Developer | Folder | Responsibility |
|-----------|--------|-----------------|
| **Najwa** | `features/credit-card/` | Credit card fraud detection (Components, Services, Pages) |
| **Ferdaouss** | `features/scam/` | Phishing/scam detection (Components, Services, Pages) |
| **Alae** | `features/visual/` | Document/invoice fraud (Components, Services, Pages) |
| **Team** | `core/`, `shared/`, `layout/` | Shared infrastructure |

---

## 📝 Notes

- Each feature module is completely independent
- Features can be lazy-loaded for better performance
- Shared components and services are in `core/` and `shared/`
- Each developer can work on their feature without conflicts
- All imports should be relative paths: `../../../` → `../../` or use barrel exports

---

## ✨ Key Files to Monitor

1. **app.routes.ts** - Main routing configuration
2. **app.ts** - Root component
3. **core/services/api.service.ts** - Base API service
4. **core/guards/auth.guard.ts** - Authentication guard
5. **layout/shell.component.ts** - Main layout

---

**Status**: ✅ Scaffolding complete. Ready for component migration.

**Next Action**: Start moving components and updating imports (coordinate with team).
