import { Component, inject, OnInit, OnDestroy } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { 
  LucideShield, 
  LucideLayoutDashboard, 
  LucideCreditCard, 
  LucideMail, 
  LucideFileText, 
  LucideHistory, 
  LucideLogOut,
  LucideActivity,
  LucideCpu,
  LucideLock,
  LucideWifi
} from '@lucide/angular';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-shell',
  standalone: true,
  imports: [
    CommonModule, 
    RouterOutlet, 
    RouterLink, 
    RouterLinkActive, 
    LucideShield, 
    LucideLayoutDashboard, 
    LucideCreditCard, 
    LucideMail, 
    LucideFileText, 
    LucideHistory, 
    LucideLogOut, 
    LucideActivity, 
    LucideCpu, 
    LucideLock, 
    LucideWifi
  ],
  templateUrl: './shell.component.html',
  styleUrl: './shell.component.scss',
})
export class ShellComponent implements OnInit, OnDestroy {
  auth = inject(AuthService);

  readonly Shield = LucideShield;
  readonly LogOut = LucideLogOut;
  readonly Activity = LucideActivity;
  readonly Cpu = LucideCpu;
  readonly Lock = LucideLock;
  readonly Wifi = LucideWifi;

  systemTime = '';
  private timer: any;

  nav = [
    { path: '/dashboard', label: 'Dashboard', icon: LucideLayoutDashboard },
    { path: '/agents/credit-card', label: 'Credit Card', icon: LucideCreditCard },
    { path: '/agents/phishing', label: 'Phishing', icon: LucideMail },
    { path: '/agents/document', label: 'Documents', icon: LucideFileText },
    { path: '/history', label: 'History', icon: LucideHistory },
  ];

  ngOnInit() {
    this.updateTime();
    this.timer = setInterval(() => this.updateTime(), 1000);
  }

  ngOnDestroy() {
    if (this.timer) clearInterval(this.timer);
  }

  private updateTime() {
    const now = new Date();
    this.systemTime = now.toLocaleTimeString('en-US', { hour12: false });
  }
}
