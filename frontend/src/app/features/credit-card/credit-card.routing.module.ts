import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'credit-card',
    loadComponent: () =>
      import('./pages/credit-card-agent/credit-card-agent.component').then(
        (m) => m.CreditCardAgentComponent
      ),
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class CreditCardRoutingModule {}
