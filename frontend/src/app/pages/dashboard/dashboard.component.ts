import { DecimalPipe, DatePipe } from '@angular/common';
import { Component, inject, OnInit, OnDestroy, signal } from '@angular/core';
import { FraudApiService } from '../../services/fraud-api.service';
import { WebsocketService } from '../../services/websocket.service';
import { AnalyticsSummary } from '../../core/models/fraud.models';
import { Subscription } from 'rxjs';
import { 
  LucideActivity, 
  LucideAlertTriangle, 
  LucideTrendingUp, 
  LucideShield, 
  LucideFileText, 
  LucideSearch, 
  LucideCheckCircle,
  LucideUsers,
  LucideClock,
  LucideBarChart3,
  LucideShieldCheck
} from '@lucide/angular';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    DecimalPipe, 
    DatePipe,
    LucideActivity, 
    LucideAlertTriangle, 
    LucideTrendingUp, 
    LucideShield, 
    LucideFileText, 
    LucideSearch, 
    LucideCheckCircle,
    LucideUsers,
    LucideClock,
    LucideBarChart3,
    LucideShieldCheck,
    CommonModule
  ],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
})
export class DashboardComponent implements OnInit, OnDestroy {
  private api = inject(FraudApiService);
  private ws = inject(WebsocketService);
  private wsSubscription?: Subscription;
  
  analytics = signal<AnalyticsSummary | null>(null);
  loading = signal(true);
  currentTime = signal(new Date());
  
  // Real-time Histogram data (Kept local for visual speed)
  histogramBars = signal<number[]>(Array.from({ length: 45 }, () => Math.floor(Math.random() * 60) + 20));

  // Agent statuses with terminal logs
  agents = signal([
    {
      id: 'credit_card',
      name: 'Credit Card Investigator',
      specialist: 'Najwa',
      tech: 'XGBoost + SHAP',
      status: 'IDLE',
      confidence: 99.96,
      logs: [] as string[]
    },
    {
      id: 'phishing',
      name: 'Phishing Scanner',
      specialist: 'Ferdaouss',
      tech: 'NLP + LLM Transformer',
      status: 'IDLE',
      confidence: 94.2,
      logs: [] as string[]
    },
    {
      id: 'document',
      name: 'Document Verifier',
      specialist: 'Alae',
      tech: 'CNN (ResNet50 CV)',
      status: 'IDLE',
      confidence: 97.8,
      logs: [] as string[]
    }
  ]);

  // XAI Drivers
  riskDrivers = signal([
    { label: 'Transaction Amount', impact: '0%' },
    { label: 'Merchant Risk Score', impact: '0%' },
    { label: 'Unusual Geo Location', impact: '0%' }
  ]);

  // Real-time inference simulation
  inferenceTime = signal(14);
  processedToday = signal(18432);

  ngOnInit(): void {
    this.load();
    
    // Connect to WebSocket Fraud Stream
    this.ws.connect('ws://localhost:8000/ws/fraud-stream');
    
    this.wsSubscription = this.ws.getMessages().subscribe(data => {
      this.updateFromWebSocket(data);
    });

    // Update digital clock
    setInterval(() => {
      this.currentTime.set(new Date());
    }, 1000);

    // Local histogram animation (Keep it smooth)
    setInterval(() => {
      this.histogramBars.update(bars => {
        const newBars = [...bars.slice(1), Math.floor(Math.random() * 60) + 20];
        return newBars;
      });
    }, 200);
  }

  ngOnDestroy(): void {
    this.wsSubscription?.unsubscribe();
    this.ws.disconnect();
  }

  private updateFromWebSocket(data: any): void {
    // Update Global Metrics
    this.processedToday.set(data.processed_today);
    this.inferenceTime.set(parseInt(data.avg_inference));
    
    // Update Agents
    this.agents.update(agents => {
      return agents.map(agent => {
        if (agent.id === 'credit_card') {
          return { ...agent, status: data.credit_card_agent.status, logs: data.credit_card_agent.terminal_lines };
        }
        if (agent.id === 'phishing') {
          return { ...agent, status: data.phishing_agent.status, logs: data.phishing_agent.terminal_lines };
        }
        if (agent.id === 'document') {
          return { ...agent, status: data.document_agent.status, logs: data.document_agent.terminal_lines };
        }
        return agent;
      });
    });

    // Update XAI Insights (Najwa's track)
    this.riskDrivers.set(data.credit_card_agent.xai_insights.top_risk_drivers.map((d: any) => ({
      label: d.name,
      impact: d.impact
    })));
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
}
