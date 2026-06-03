import { Injectable } from '@angular/core';
import { FraudApiService } from '../../../services/fraud-api.service';

@Injectable({
  providedIn: 'root',
})
export class VisualService {
  constructor(private fraudApi: FraudApiService) {}

  verify(file: File) {
    return this.fraudApi.verifyDocument(file);
  }
}
