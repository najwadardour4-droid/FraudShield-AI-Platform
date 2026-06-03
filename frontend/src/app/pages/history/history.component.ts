import { DatePipe, DecimalPipe } from '@angular/common';
import { Component, inject, OnInit, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HistoryItem } from '../../core/models/fraud.models';
import { FraudApiService } from '../../services/fraud-api.service';
import { LucideSearch } from '@lucide/angular';

@Component({
  selector: 'app-history',
  standalone: true,
  imports: [FormsModule, DatePipe, DecimalPipe, LucideSearch],
  templateUrl: './history.component.html',
  styleUrl: './history.component.scss',
})
export class HistoryComponent implements OnInit {
  private api = inject(FraudApiService);
  items = signal<HistoryItem[]>([]);
  filter = '';
  loading = signal(true);

  readonly Search = LucideSearch;

  ngOnInit(): void {
    this.load();
  }

  load(): void {
    this.loading.set(true);
    this.api.getHistory(this.filter || undefined).subscribe({
      next: (rows) => {
        this.items.set(rows);
        this.loading.set(false);
      },
      error: () => this.loading.set(false),
    });
  }

  agentLabel(agent?: string): string {
    const map: Record<string, string> = {
      credit_card: 'Najwa',
      phishing: 'Ferdaouss',
      document: 'Alae',
      orchestrator: 'Orchestrator',
    };
    return agent ? (map[agent] ?? agent) : '—';
  }
}
