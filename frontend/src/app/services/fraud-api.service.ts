import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import {
  AgentPrediction,
  AnalyticsSummary,
  CreditCardInput,
  HistoryItem,
} from '../core/models/fraud.models';

@Injectable({ providedIn: 'root' })
export class FraudApiService {
  private base = environment.apiUrl;

  constructor(private http: HttpClient) {}

  predictCreditCard(data: CreditCardInput): Observable<AgentPrediction> {
    return this.http.post<AgentPrediction>(`${this.base}/credit-card-fraud/predict`, data);
  }

  scanPhishing(text: string, channel = 'email'): Observable<AgentPrediction> {
    return this.http.post<AgentPrediction>(`${this.base}/phishing-detection/scan`, { text, channel });
  }

  verifyDocument(file: File): Observable<AgentPrediction> {
    const form = new FormData();
    form.append('file', file);
    return this.http.post<AgentPrediction>(`${this.base}/document-verification/verify`, form);
  }

  getAnalytics(): Observable<AnalyticsSummary> {
    return this.http.get<AnalyticsSummary>(`${this.base}/analytics/summary`);
  }

  getHistory(agent?: string, limit = 100): Observable<HistoryItem[]> {
    const params: Record<string, string> = { limit: String(limit) };
    if (agent) params['agent'] = agent;
    return this.http.get<HistoryItem[]>(`${this.base}/history`, { params });
  }
}
