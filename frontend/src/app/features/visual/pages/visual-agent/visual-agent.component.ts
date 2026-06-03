import { Component, inject, signal } from '@angular/core';
import { AgentPrediction } from '../../../../core/models/fraud.models';
import { FraudApiService } from '../../../../services/fraud-api.service';
import { PredictionResultComponent } from '../../../../shared/prediction-result.component';

@Component({
  selector: 'app-visual-agent',
  standalone: true,
  imports: [PredictionResultComponent],
  templateUrl: './visual-agent.component.html',
  styleUrl: './visual-agent.component.scss',
})
export class VisualAgentComponent {
  private api = inject(FraudApiService);

  loading = signal(false);
  result = signal<AgentPrediction | null>(null);
  error = signal('');
  preview = signal<string | null>(null);

  onFile(e: Event): void {
    const input = e.target as HTMLInputElement;
    const file = input.files?.[0];
    if (!file) return;
    this.preview.set(URL.createObjectURL(file));
    this.analyze(file);
  }

  onDrop(e: DragEvent): void {
    e.preventDefault();
    const file = e.dataTransfer?.files?.[0];
    if (file) {
      this.preview.set(URL.createObjectURL(file));
      this.analyze(file);
    }
  }

  analyze(file: File): void {
    this.loading.set(true);
    this.error.set('');
    this.result.set(null);
    this.api.verifyDocument(file).subscribe({
      next: (r) => {
        this.result.set({
          agent: r.agent || 'document_verifier',
          verdict: r.verdict,
          confidence: r.confidence,
          explanation: r.explanation,
          anomalies: r.anomalies,
          record_id: r.record_id,
        });
        this.loading.set(false);
      },
      error: (e) => {
        this.error.set(e?.error?.detail || 'Verification failed.');
        this.loading.set(false);
      },
    });
  }
}
