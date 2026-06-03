import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { InvoiceService } from '../../../../services/invoice.service';
import { GradCamComponent } from '../grad-cam/grad-cam.component';
import { ParticleFieldComponent } from '../../../../components/particle-field/particle-field.component';

@Component({
  standalone: true,
  selector: 'app-invoice-guard',
  imports: [CommonModule, FormsModule, GradCamComponent, ParticleFieldComponent],
  templateUrl: './invoice-guard.component.html',
  styleUrls: ['./invoice-guard.component.scss']
})
export class InvoiceGuardComponent {
  role = 'user';
  form = { email: 'alice@corp.ma', password: 'user123' };
  loading = false;
  focused: string | null = null;

  constructor(private invoiceSvc: InvoiceService) {}

  switchRole(r: string) {
    this.role = r;
    this.form = { email: r === 'admin' ? 'admin@invoiceguard.ai' : 'alice@corp.ma', password: r === 'admin' ? 'admin123' : 'user123' };
  }

  handleLogin() {
    this.loading = true;
    setTimeout(() => { this.loading = false; console.log('logged', this.role, this.form.email); }, 1200);
  }

  onFileSelected(evt: Event) {
    const target = evt.target as HTMLInputElement;
    const file = target.files && target.files[0];
    if (file) this.startAnalysis(file);
  }

  startAnalysis(file: File) {
    this.invoiceSvc.analyzeInvoice(file).subscribe((res: any) => console.log('analysis', res));
  }

  onDrop(e: DragEvent) {
    e.preventDefault();
    const files = e.dataTransfer?.files;
    if (files && files.length) this.startAnalysis(files[0]);
  }
  onDragOver(e: DragEvent) { e.preventDefault(); }
}
