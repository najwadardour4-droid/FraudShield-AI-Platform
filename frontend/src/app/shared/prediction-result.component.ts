import { DecimalPipe } from '@angular/common';
import { Component, computed, input } from '@angular/core';
import { AgentPrediction } from '../core/models/fraud.models';

@Component({
  selector: 'app-prediction-result',
  standalone: true,
  imports: [DecimalPipe],
  templateUrl: './prediction-result.component.html',
  styleUrl: './prediction-result.component.scss',
})
export class PredictionResultComponent {
  result = input.required<AgentPrediction>();
  readonly Math = Math;

  isRisk = computed(() => this.result().verdict === 'FRAUD' || this.result().verdict === 'FAKE' || this.result().verdict === 'SUSPECTE' || this.result().verdict === 'PHISHING');

  shapFeatures = computed(() => {
    const res = this.result() as any;
    const details = res.technical_details as any;
    const shap = res.shap_values || details?.shap_values;
    if (!shap) return [];
    
    return Object.entries(shap)
      .map(([name, value]) => ({ name, value: value as number }))
      .sort((a, b) => Math.abs(b.value) - Math.abs(a.value))
      .slice(0, 5);
  });
}
