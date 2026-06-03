import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'phishing',
    loadComponent: () =>
      import('./pages/scam-agent/scam-agent.component').then(
        (m) => m.ScamAgentComponent
      ),
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ScamRoutingModule {}
