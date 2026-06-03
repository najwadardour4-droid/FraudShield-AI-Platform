import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-credit-card-agent',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './credit-card-agent.component.html',
  styleUrl: './credit-card-agent.component.scss',
})
export class CreditCardAgentComponent {

  transaction = {
    amount: 100,
    hour_of_day: 14,
    distance_from_home_km: 10,
    v1: 0,
    v2: 0,
    v3: 0
  };

  result: any = null;

  analyze() {
    console.log(this.transaction);

    // هنا من بعد غادي نعيطو لل API
    this.result = {
      verdict: 'FRAUD',
      confidence: 0.98,
      risk_score: 0.95
    };
  }
}