import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AgentPrediction } from '../../../core/models/fraud.models';
import { FraudApiService } from '../../../services/fraud-api.service';
import { PredictionResultComponent } from '../../../shared/prediction-result.component';
import { LucideMail } from '@lucide/angular';

@Component({
  selector: 'app-phishing',
  standalone: true,
  imports: [FormsModule, PredictionResultComponent, LucideMail],
  templateUrl: './phishing.component.html',
  styleUrl: './phishing.component.scss',
})
export class PhishingComponent {
  private api = inject(FraudApiService);
  loading = signal(false);
  result = signal<AgentPrediction | null>(null);
  error = signal('');
  text = '';
  channel = 'email';

  onFileSelected(evt: Event) {
    const target = evt.target as HTMLInputElement;
    const file = target.files?.[0];
    if (!file) return;

    // Simulate file reading and header extraction
    this.text = `[ANALYZING FILE: ${file.name}]\n--------------------------\n(Extracted Content Simulation)\nSubject: Suspicious Transaction Alert\nFrom: security-verify@bank-support-desk.com\nTo: user@domain.com\n\nBody: Please click the link below to verify your account activity...`;
  }

  analyze(): void {
    if (!this.text) return;
    this.loading.set(true);
    this.error.set('');
    this.result.set(null);
    this.api.scanPhishing(this.text, this.channel).subscribe({
      next: (res) => {
        this.result.set(res);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set(err.error?.detail || 'Analysis failed');
        this.loading.set(false);
      },
    });
  }
}
