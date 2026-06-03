import { Routes } from '@angular/router';
import { authGuard, guestGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  {
    path: 'login',
    loadComponent: () => import('./pages/login/login.component').then((m) => m.LoginComponent),
    canActivate: [guestGuard],
  },
  {
    path: '',
    loadComponent: () => import('./layout/shell.component').then((m) => m.ShellComponent),
    canActivate: [authGuard],
    children: [
      {
        path: 'dashboard',
        loadComponent: () => import('./pages/dashboard/dashboard.component').then((m) => m.DashboardComponent),
      },
      {
        path: 'agents/credit-card',
        loadComponent: () =>
          import('./pages/agents/credit-card/credit-card.component').then((m) => m.CreditCardAgentComponent),
      },
      {
        path: 'agents/phishing',
        loadComponent: () =>
          import('./pages/agents/phishing/phishing.component').then((m) => m.PhishingComponent),
      },
      {
        path: 'agents/document',
        loadComponent: () =>
          import('./pages/agents/document/document.component').then((m) => m.DocumentComponent),
      },
      {
        path: 'history',
        loadComponent: () => import('./pages/history/history.component').then((m) => m.HistoryComponent),
      },
    ],
  },
  { path: '**', redirectTo: 'dashboard' },
];
