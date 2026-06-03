import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-grad-cam',
  imports: [CommonModule],
  templateUrl: './grad-cam.component.html',
  styleUrls: ['./grad-cam.component.scss']
})
export class GradCamComponent {
  @Input() invoiceId?: string;

  // pattern copied from the original React source
  pats: number[] = [
    0,0,1,2,3,5,4,3,2,1,0,0, 0,1,2,4,6,7,6,4,2,1,0,0, 0,1,3,5,7,8,7,5,3,1,0,0,
    0,0,2,4,6,7,6,3,1,0,1,1, 0,0,1,2,4,5,4,2,0,0,1,2, 0,0,0,1,2,3,2,1,0,0,1,2,
    0,0,0,0,1,2,1,0,0,0,0,1, 0,0,0,0,0,1,0,0,0,0,0,0
  ];

  cs: string[] = [
    '#060c12','#0a1520','#0d2030','rgba(255,184,0,.2)','rgba(255,184,0,.5)',
    'rgba(255,77,106,.4)','rgba(255,77,106,.7)','#FF4D6A','#dc2020'
  ];

  get flat(): number[] {
    const seed = this.invoiceId ? this.invoiceId.charCodeAt(this.invoiceId.length - 1) % 3 : 0;
    return this.pats.map(v => Math.min(v + seed, 8));
  }
}
