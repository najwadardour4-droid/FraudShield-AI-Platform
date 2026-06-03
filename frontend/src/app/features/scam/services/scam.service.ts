import { Injectable } from '@angular/core';
import { FraudApiService } from '../../../services/fraud-api.service';

@Injectable({
  providedIn: 'root',
})
export class ScamService {
  constructor(private fraudApi: FraudApiService) {}

  scan(text: string) {
    return this.fraudApi.scanPhishing(text);
  }
}
