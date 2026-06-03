import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-score-ring',
  imports: [CommonModule],
  template: `
    <div class="ring-container" [style.width.px]="size" [style.height.px]="size">
      <svg [attr.width]="size" [attr.height]="size" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="45" fill="none" stroke="rgba(0, 242, 255, 0.05)" stroke-width="8"></circle>
        <circle cx="50" cy="50" r="45" fill="none" [attr.stroke]="col" stroke-width="8"
          [attr.stroke-dasharray]="282.7" [attr.stroke-dashoffset]="282.7 - (282.7 * score / 100)" 
          stroke-linecap="round" [ngStyle]="{filter: 'drop-shadow(0 0 8px ' + col + ')'}"
          style="transition: stroke-dashoffset 1s ease-out; transform: rotate(-90deg); transform-origin: center;"></circle>
      </svg>
      <div class="ring-content">
        <span class="score-value" [style.color]="col">{{score}}</span>
        <span class="score-label" [style.color]="col">RISK</span>
      </div>
    </div>
  `,
  styles: [`
    .ring-container { position: relative; display: flex; align-items: center; justify-content: center; }
    .ring-content { position: absolute; display: flex; flex-direction: column; align-items: center; text-align: center; }
    .score-value { font-family: 'Orbitron', sans-serif; font-size: 1.5rem; font-weight: 800; line-height: 1; }
    .score-label { font-family: 'JetBrains Mono', monospace; font-size: 0.5rem; letter-spacing: 1px; margin-top: 2px; }
  `]
})
export class ScoreRingComponent {
  @Input() score = 0;
  @Input() size = 120;

  get col() { 
    if (this.score >= 70) return '#ff4d6a'; // Danger Neon
    if (this.score >= 40) return '#ffb800'; // Warning Neon
    return '#00f2ff'; // Primary Neon
  }
}
