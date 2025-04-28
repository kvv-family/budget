import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { ConfigService } from './config.service';
import { HttpBackend, HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  token: string | undefined;
  statusAuth: Subject<boolean> = new Subject();

  private httpBackEnd: HttpClient;

  constructor(private config: ConfigService, public handler: HttpBackend) {
    this.httpBackEnd = new HttpClient(handler);
  }

  checkUser(): boolean {
    const token = localStorage.getItem('authToken');
    if (!token) {
      console.warn('Нет токена авторизации');
      this.statusAuth.next(false);
      return false;
    }

    return true;
  }

  addToken(token: string) {
    localStorage.setItem('authToken', token);
    this.statusAuth.next(true);
  }

  removeToken() {
    localStorage.removeItem('authToken');
    this.statusAuth.next(false);
  }
}
