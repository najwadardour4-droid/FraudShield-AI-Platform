import { Component } from '@angular/core';

@Component({
  selector: 'app-card-investigator',
  templateUrl: './card-investigator.component.html',
  styleUrls: ['./card-investigator.component.scss']
})
export class CardInvestigatorComponent {
  // Data dyal s-7abatek + dyalk
  invoices = [
    { id: "FACT-2026-00891", vendor: "BTP Maroc", amount: 18400, score: 94, status: "fraud" },
    { id: "FACT-2026-00834", vendor: "LogiTech Pro", amount: 7250, score: 87, status: "fraud" }
  ];

  getScoreColor(score: number): string {
    if (score >= 70) return '#FF4D6A'; // Coral
    if (score >= 40) return '#FFB800'; // Amber
    return '#00FFD1'; // Teal
  }
}