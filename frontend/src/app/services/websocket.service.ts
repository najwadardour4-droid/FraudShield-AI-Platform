import { Injectable, signal } from '@angular/core';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WebsocketService {
  private socket?: WebSocket;
  private messageSubject = new Subject<any>();
  public isConnected = signal(false);

  constructor() { }

  connect(url: string): void {
    if (this.socket) {
      this.socket.close();
    }

    this.socket = new WebSocket(url);

    this.socket.onopen = () => {
      console.log('WebSocket Connected to Fraud Stream');
      this.isConnected.set(true);
    };

    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.messageSubject.next(data);
    };

    this.socket.onclose = () => {
      console.log('WebSocket Disconnected');
      this.isConnected.set(false);
      // Attempt reconnection after 5 seconds
      setTimeout(() => this.connect(url), 5000);
    };

    this.socket.onerror = (error) => {
      console.error('WebSocket Error:', error);
      this.socket?.close();
    };
  }

  getMessages(): Observable<any> {
    return this.messageSubject.asObservable();
  }

  disconnect(): void {
    this.socket?.close();
  }
}
