import { ApplicationConfig, provideZoneChangeDetection, APP_INITIALIZER } from '@angular/core';
import { provideRouter } from '@angular/router';
import { providePrimeNG } from 'primeng/config';
import Aura from '@primeng/themes/aura';
import { routes } from './app.routes';
import { ConfigService } from './services/config.service';
import { provideHttpClient } from '@angular/common/http';
import { AuthService } from './services/auth.service';
import { AuthGuard } from './guards/auth.guard';

export const appConfig: ApplicationConfig = {
  providers: [provideZoneChangeDetection({ eventCoalescing: true }), provideRouter(routes), provideHttpClient(), providePrimeNG({
    theme: {
      preset: Aura
    }
  }),
  {
      provide: APP_INITIALIZER,
      multi: true,
      deps: [ConfigService],
      useFactory: (config: ConfigService, auth: AuthService) => {
        return () => {
          return config.loadConfig();
        }
      }
    },
    AuthGuard
  ]
};
