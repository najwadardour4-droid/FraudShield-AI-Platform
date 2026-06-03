import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { LucideShield, LucideMail, LucideLock, LucideAlertCircle, LucideShieldCheck } from '@lucide/angular';
import { ParticleFieldComponent } from '../../components/particle-field/particle-field.component';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    FormsModule, 
    LucideShield, 
    LucideMail, 
    LucideLock, 
    LucideAlertCircle, 
    LucideShieldCheck, 
    ParticleFieldComponent
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
})
export class LoginComponent {
  private auth = inject(AuthService);
  private router = inject(Router);

  email = 'admin@fraudshield.ai';
  password = 'admin123';
  loading = signal(false);
  error = signal('');

  submit(): void {
    if (!this.email.endsWith('@fraudshield.ai')) {
      this.error.set('Access Denied. Internal domain accounts only.');
      return;
    }

    this.loading.set(true);
    this.error.set('');
    this.auth.login({ email: this.email, password: this.password }).subscribe({
      next: () => {
        if (this.email.startsWith('najwa')) {
          this.router.navigate(['/agents/credit-card']);
        } else if (this.email.startsWith('ferdaouss')) {
          this.router.navigate(['/agents/phishing']);
        } else if (this.email.startsWith('alae')) {
          this.router.navigate(['/agents/document']);
        } else {
          this.router.navigate(['/dashboard']);
        }
      },
      error: () => {
        this.error.set('Invalid credentials. Access restricted to authorized personnel.');
        this.loading.set(false);
      },
      complete: () => this.loading.set(false),
    });
  }
}
