import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AgentPrediction } from '../../../core/models/fraud.models';
import { FraudApiService } from '../../../services/fraud-api.service';
import { PredictionResultComponent } from '../../../shared/prediction-result.component';

@Component({
  selector: 'app-credit-card-agent',
  standalone: true,
  imports: [FormsModule, PredictionResultComponent],
  templateUrl: './credit-card.component.html',
  styleUrl: './credit-card.component.scss',
})
export class CreditCardAgentComponent {
  private api = inject(FraudApiService);

  step = signal<'card' | 'details'>('card');
  cardNumber = '';
  
  form = {
    amount: 8500,
    merchant_category: 'online_retail',
    hour_of_day: 2,
    distance_from_home_km: 380,
    v1: 0.1,
    v2: -0.3,
    v3: 0.05,
  };
  loading = signal(false);
  result = signal<AgentPrediction | null>(null);
  error = signal('');

  verifyCard() {
    if (this.cardNumber.length >= 16) {
      this.step.set('details');
    } else {
      this.error.set('PLEASE ENTER A VALID 16-DIGIT CARD NUMBER');
    }
  }

  reset() {
    this.step.set('card');
    this.cardNumber = '';
    this.result.set(null);
    this.error.set('');
  }

  analyze(): void {
    this.loading.set(true);
    this.error.set('');
    this.result.set(null);
    this.api.predictCreditCard(this.form).subscribe({
      next: (r) => {
        this.result.set(r);
        this.loading.set(false);
      },
      error: (e) => {
        this.error.set(e?.error?.detail || 'Prediction failed. Is the backend running?');
        this.loading.set(false);
      },
    });
  }
}
