import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AgentPrediction } from '../../../core/models/fraud.models';
import { FraudApiService } from '../../../services/fraud-api.service';
import { PredictionResultComponent } from '../../../shared/prediction-result.component';

@Component({
  selector: 'app-document',
  standalone: true,
  imports: [FormsModule, PredictionResultComponent, CommonModule],
  templateUrl: './document.component.html',
  styleUrl: './document.component.scss',
})
export class DocumentComponent {
  private api = inject(FraudApiService);

  loading = signal(false);
  result = signal<AgentPrediction | null>(null);
  error = signal('');
  imagePreview = signal<string | null>(null);

  onFile(e: Event): void {
    const input = e.target as HTMLInputElement;
    const file = input.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = () => this.imagePreview.set(reader.result as string);
    reader.readAsDataURL(file);

    this.analyze(file);
  }

  onDrop(e: DragEvent): void {
    e.preventDefault();
    const file = e.dataTransfer?.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => this.imagePreview.set(reader.result as string);
      reader.readAsDataURL(file);

      this.analyze(file);
    }
  }

  analyze(file: File): void {
    this.loading.set(true);
    this.error.set('');
    this.result.set(null);
    this.api.verifyDocument(file).subscribe({
      next: (res) => {
        this.result.set(res);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set(err?.error?.detail || 'Analysis failed');
        this.loading.set(false);
      },
    });
  }
}
