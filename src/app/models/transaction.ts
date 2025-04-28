import { Category } from './category';

export interface Transaction {
  id: number;
  date: Date;
  amount: number;
  category: Category;
  account: string;
}
