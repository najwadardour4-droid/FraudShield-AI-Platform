import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ScoreRingComponent } from '../score-ring/score-ring.component';

@Component({
  standalone: true,
  selector: 'app-inv-modal',
  imports: [CommonModule, ScoreRingComponent],
  templateUrl: './inv-modal.component.html',
  styleUrls: ['./inv-modal.component.scss']
})
export class InvModalComponent {
  @Input() inv: any = null;
  @Output() close = new EventEmitter<void>();

  statusLabel(s: string) { return s === 'fraud' ? 'FRAUDE' : s === 'suspect' ? 'SUSPECT' : 'NORMAL'; }
  fmtEur(n: number) { return new Intl.NumberFormat('fr-MA',{style:'currency',currency:'EUR',maximumFractionDigits:0}).format(n); }
}
