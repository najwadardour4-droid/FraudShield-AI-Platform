import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  post(endpoint: string, data: any) {
    return this.http.post(`${this.baseUrl}${endpoint}`, data);
  }

  get(endpoint: string) {
    return this.http.get(`${this.baseUrl}${endpoint}`);
  }
}