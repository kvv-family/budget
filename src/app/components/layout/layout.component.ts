import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MenuItem } from 'primeng/api';
import { MenubarModule } from 'primeng/menubar';

@Component({
  selector: 'app-layout',
  imports: [RouterOutlet, MenubarModule],
  templateUrl: './layout.component.html',
  styleUrl: './layout.component.scss',
})
export class LayoutComponent {
  items: MenuItem[] = [
    {
      label: 'Главная',
      icon: 'pi pi-home',
      routerLink: '/',
    },
    {
      label: 'Транзакции',
      icon: 'pi pi-briefcase',
      items: [
        {
          label: 'Все транзакции',
          icon: 'pi pi-dollar',
          routerLink: '/transactions',
        },
        {
          label: 'Доходы',
          icon: 'pi pi-caret-up',
          routerLink: '/transactions/income',
        },
        {
          label: 'Расходы',
          icon: 'pi pi-caret-down',
          routerLink: '/transactions/expense',
        },
      ],
    },
    {
      label: 'Счета',
      icon: 'pi pi-credit-card',
    },
    {
      label: 'Сервисы',
      icon: 'pi pi-hashtag',
      items: [
        {
          label: 'Цели',
          icon: 'pi pi-crown',
        },
        {
          label: 'Бюджет',
          icon: 'pi pi-money-bill',
        },
      ],
    },
    {
      label: 'Настройки',
      icon: 'pi pi-cog',
      items: [
        {
          label: 'Общие',
          icon: 'pi pi-cog',
        },
        {
          label: 'Справочники',
          icon: 'pi pi-book',
        },
      ],
    },
    {
      label: 'Анализ',
      icon: 'pi pi-chart-bar',
      routerLink: '/analysis',
    },
  ];
}
