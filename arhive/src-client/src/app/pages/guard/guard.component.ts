import { Component } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { ConfigService } from '../../services/config.service';

@Component({
  selector: 'app-guard',
  imports: [ButtonModule, CardModule],
  templateUrl: './guard.component.html',
  styleUrl: './guard.component.scss'
})
export class GuardComponent {

  constructor(private config: ConfigService) {}

  localeClick() {
    const localeConfigProvide = this.config.getProvideConfiguration("locale");
    const localeConfig = this.config.params.providers.locale;
    if (localeConfigProvide && 'issuer' in localeConfigProvide) {
      const windows_url = new URL(window.location.href);
      const redirectUrl = windows_url.origin + localeConfig.redirect_url;
      const loginUrl = `${localeConfigProvide.authorization_endpoint}?client_id=${localeConfig.client_id}&scope=${localeConfig.scope}&state=${6374839}&redirect_uri=${redirectUrl}`;
      window.location.href = loginUrl;
    }
  }
}
