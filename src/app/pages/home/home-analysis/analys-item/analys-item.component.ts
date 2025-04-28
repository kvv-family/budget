import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-analys-item',
  imports: [],
  templateUrl: './analys-item.component.html',
  styleUrl: './analys-item.component.scss',
})
export class AnalysItemComponent {
  @Input() type: 'balance' | 'income' | 'expense' = 'balance';
  @Input() balance: number = 0;
  @Input() diff: number = 0;
}
