import { HttpClient } from '@angular/common/http';
import { Injectable, signal } from '@angular/core';
import { Router } from '@angular/router';
import { Observable, tap } from 'rxjs';
import { environment } from '../../environments/environment';
import { AuthUser, LoginRequest } from '../core/models/fraud.models';

const STORAGE_KEY = 'fraudshield_auth';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly userState = signal<AuthUser | null>(this.loadStored());

  constructor(
    private http: HttpClient,
    private router: Router,
  ) {}

  user = this.userState.asReadonly();

  token(): string | null {
    return this.userState()?.access_token ?? null;
  }

  isLoggedIn(): boolean {
    return !!this.userState()?.access_token;
  }

  login(credentials: LoginRequest): Observable<AuthUser> {
    return this.http.post<AuthUser>(`${environment.apiUrl}/auth/login`, credentials).pipe(
      tap((res) => {
        this.userState.set(res);
        localStorage.setItem(STORAGE_KEY, JSON.stringify(res));
      }),
    );
  }

  logout(): void {
    this.userState.set(null);
    localStorage.removeItem(STORAGE_KEY);
    this.router.navigate(['/login']);
  }

  private loadStored(): AuthUser | null {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? (JSON.parse(raw) as AuthUser) : null;
    } catch {
      return null;
    }
  }
}
