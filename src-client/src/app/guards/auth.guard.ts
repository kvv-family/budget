import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from '@angular/router';
import { AuthService } from '../services/auth.service';

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(private auth: AuthService, private router: Router) {
    
  }

  canActivate(next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot) {
      const stateAuth = this.auth.checkUser();
      if (!stateAuth) {
        this.router.navigate(["guard"]);
      }
      return true
    }
}
