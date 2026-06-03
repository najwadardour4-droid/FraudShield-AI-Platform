import { DecimalPipe } from '@angular/common';
import { Component, inject, OnInit, signal } from '@angular/core';
import { FraudApiService } from '../../services/fraud-api.service';
import { AnalyticsSummary } from '../../core/models/fraud.models';
import { LucideActivity, LucideAlertTriangle, LucideTrendingUp } from '@lucide/angular';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [DecimalPipe, LucideActivity, LucideAlertTriangle, LucideTrendingUp, CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
})
export class DashboardComponent implements OnInit {
  private api = inject(FraudApiService);
  analytics = signal<AnalyticsSummary | null>(null);
  loading = signal(true);

  readonly Activity = LucideActivity;
  readonly AlertTriangle = LucideAlertTriangle;
  readonly TrendingUp = LucideTrendingUp;
  readonly Math = Math;

  waveformBars = signal<number[]>(Array.from({ length: 20 }, () => Math.floor(Math.random() * 60) + 20));

  ngOnInit(): void {
    this.load();
    setInterval(() => {
      this.waveformBars.set(Array.from({ length: 20 }, () => Math.floor(Math.random() * 60) + 20));
    }, 150);
  }

  load() {
    this.api.getAnalytics().subscribe({
      next: (data) => {
        this.analytics.set(data);
        this.loading.set(false);
      },
      error: () => this.loading.set(false),
    });
  }

  agentLabel(agent: string): string {
    const map: Record<string, string> = {
      credit_card: 'Najwa — Credit Card',
      phishing: 'Ferdaouss — Phishing',
      document: 'Alae — Documents',
      orchestrator: 'Orchestrator',
    };
    return map[agent] ?? agent;
  }

  barWidth(flagged: number, total: number): number {
    if (!total) return 0;
    return Math.round((flagged / total) * 100);
  }
}
