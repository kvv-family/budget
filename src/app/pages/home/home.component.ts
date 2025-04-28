import { Component } from '@angular/core';
import { HomeAnalysisComponent } from './home-analysis/home-analysis.component';
import { TransactionsComponent } from './transactions/transactions.component';
@Component({
  selector: 'app-home',
  imports: [HomeAnalysisComponent, TransactionsComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss',
})
export class HomeComponent {}
