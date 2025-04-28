import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-callback',
  imports: [],
  templateUrl: './callback.component.html',
  styleUrl: './callback.component.scss',
})
export class CallbackComponent implements OnInit {
  token: string | null = null;
  constructor(private route: ActivatedRoute, private auth: AuthService) {}

  ngOnInit() {
    this.route.queryParams.subscribe((params: any) => {
      if (params.token) {
        this.token = params.token;
        console.debug('Токен авторизации', this.token);
      }
      if (this.token) {
        this.auth.addToken(this.token);
      }
    });
  }
}
