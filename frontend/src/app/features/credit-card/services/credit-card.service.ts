import { Injectable } from '@angular/core';
import { FraudApiService } from '../../../services/fraud-api.service';

@Injectable({
  providedIn: 'root',
})
export class CreditCardService {
  constructor(private fraudApi: FraudApiService) {}

  predict(data: any) {
    return this.fraudApi.predictCreditCard(data);
  }
}
