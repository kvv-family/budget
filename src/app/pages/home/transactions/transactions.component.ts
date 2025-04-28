import { Component } from '@angular/core';
import { TableModule } from 'primeng/table';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { Transaction } from '../../../models/transaction';
import { DatePipe } from '@angular/common';
import { TextareaModule } from 'primeng/textarea';
import { InputTextModule } from 'primeng/inputtext';
import { InputNumberModule } from 'primeng/inputnumber';
import { FloatLabelModule } from 'primeng/floatlabel';
import { DatePickerModule } from 'primeng/datepicker';
import { SelectModule } from 'primeng/select';
import { SelectButtonModule } from 'primeng/selectbutton';

@Component({
  selector: 'app-transactions',
  imports: [
    TableModule,
    ButtonModule,
    CardModule,
    DatePipe,
    TextareaModule,
    InputTextModule,
    InputNumberModule,
    FloatLabelModule,
    DatePickerModule,
    SelectModule,
    SelectButtonModule,
  ],
  templateUrl: './transactions.component.html',
  styleUrl: './transactions.component.scss',
})
export class TransactionsComponent {
  transactions: Transaction[] = [
    {
      id: 1,
      date: new Date('2021-01-01'),
      amount: 100,
      category: {
        id: 1,
        name: 'Food',
        color: '#FF0000',
      },
      account: '1234567890',
    },
  ];
  typeTransaction = [
    {
      label: 'Расход',
      value: 'expense',
    },
    {
      label: 'Доход',
      value: 'income',
    },
  ];
}
