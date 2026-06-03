export interface LoginRequest {
  email: string;
  password: string;
}

export interface AuthUser {
  access_token: string;
  email: string;
  full_name: string;
  role: string;
}

export interface AgentPrediction {
  agent: string;
  verdict: string;
  confidence: number;
  explanation: string;
  risk_score?: number; // 0-100 Criticality Scale (Najwa)
  technical_details?: Record<string, unknown>;
  record_id?: number;
  anomalies?: string[];
}

export interface CreditCardInput {
  amount: number;
  merchant_category: string;
  hour_of_day: number;
  distance_from_home_km: number;
  v1: number;
  v2: number;
  v3: number;
}

export interface HistoryItem {
  id: number;
  agent_type?: string;
  verdict: string;
  confidence: number;
  input_summary: string;
  explanation: string;
  created_at: string | null;
}

export interface AnalyticsSummary {
  total_predictions: number;
  total_flagged: number;
  by_agent: { agent: string; total: number; flagged: number; avg_confidence: number }[];
  recent_flagged: { id: number; agent: string; verdict: string; confidence: number; summary: string; created_at: string | null }[];
}
