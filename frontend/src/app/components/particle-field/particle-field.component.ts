import { Component, AfterViewInit, OnDestroy, ElementRef, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-particle-field',
  imports: [CommonModule],
  templateUrl: './particle-field.component.html',
  styleUrls: ['./particle-field.component.scss']
})
export class ParticleFieldComponent implements AfterViewInit, OnDestroy {
  @ViewChild('canvas', { static: true }) canvasRef!: ElementRef<HTMLCanvasElement>;
  private rafId = 0;
  private particles: Array<any> = [];

  ngAfterViewInit(): void {
    const canvas = this.canvasRef.nativeElement;
    const ctx = canvas.getContext('2d')!;

    const resize = () => {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
    };
    resize();

    const W = () => canvas.width;
    const H = () => canvas.height;

    this.particles = Array.from({ length: 80 }, () => ({
      x: Math.random() * W(), y: Math.random() * H(),
      vx: (Math.random() - 0.5) * 0.4, vy: (Math.random() - 0.5) * 0.4,
      r: Math.random() * 1.5 + 0.3,
      a: Math.random(),
      color: Math.random() > 0.6 ? '#00FFD1' : Math.random() > 0.5 ? '#FFB800' : '#FF4D6A',
    }));

    const draw = () => {
      ctx.fillStyle = 'rgba(2,5,9,0.25)';
      ctx.fillRect(0, 0, W(), H());

      this.particles.forEach(p => {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0) p.x = W(); if (p.x > W()) p.x = 0;
        if (p.y < 0) p.y = H(); if (p.y > H()) p.y = 0;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = p.a * 0.6;
        ctx.fill();
        ctx.globalAlpha = 1;
      });

      for (let i = 0; i < this.particles.length; i++) {
        const a = this.particles[i];
        for (let j = i + 1; j < this.particles.length; j++) {
          const b = this.particles[j];
          const d = Math.hypot(a.x - b.x, a.y - b.y);
          if (d < 80) {
            ctx.beginPath();
            ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y);
            ctx.strokeStyle = '#00FFD1';
            ctx.globalAlpha = (1 - d / 80) * 0.12;
            ctx.lineWidth = 0.5;
            ctx.stroke();
            ctx.globalAlpha = 1;
          }
        }
      }

      this.rafId = requestAnimationFrame(draw);
    };

    this.rafId = requestAnimationFrame(draw);
    window.addEventListener('resize', resize);
  }

  ngOnDestroy(): void {
    cancelAnimationFrame(this.rafId);
  }
}
