import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'document',
    loadComponent: () =>
      import('./pages/visual-agent/visual-agent.component').then(
        (m) => m.VisualAgentComponent
      ),
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class VisualRoutingModule {}
