import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthServiceService } from './auth-service.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthServiceService, private router: Router) {}

  canActivate(): boolean {
    console.log('AuthGuard canActivate() invoked');
    if (!this.authService.isLoggedIn()) {
      console.log('Not logged in');
      if (this.authService.checkStoredSession()) {
        console.log('Stored session found');
        return true;
      } else {
        console.log('No stored session, redirecting to /login');
        this.router.navigate(['/login']);
        return false;
      }
    }
    console.log('Logged in');
    return true;
  }
  
}
