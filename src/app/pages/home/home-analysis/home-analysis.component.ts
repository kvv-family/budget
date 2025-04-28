import { Component } from '@angular/core';
import { CardModule } from 'primeng/card';
import { AnalysItemComponent } from './analys-item/analys-item.component';

@Component({
  selector: 'app-home-analysis',
  imports: [CardModule, AnalysItemComponent],
  templateUrl: './home-analysis.component.html',
  styleUrl: './home-analysis.component.scss',
})
export class HomeAnalysisComponent {
}
