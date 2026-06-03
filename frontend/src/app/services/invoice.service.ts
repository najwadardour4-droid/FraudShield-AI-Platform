import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class InvoiceService {
  // Stubbed service: replace with HttpClient calls to your backend when ready
  analyzeInvoice(file: File): Observable<any> {
    console.log('InvoiceService.analyzeInvoice called', file.name);
    return of({ status: 'ok', id: `FACT-2026-${Math.floor(Math.random()*9000+1000)}` });
  }
}
