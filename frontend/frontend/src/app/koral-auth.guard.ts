import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class KoralAuthGuard implements CanActivate {

  constructor(private router: Router) {}

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
      // Redirect to an unauthorized page or another route
      this.router.navigate(['/main']); 
      return false; // Always deny access to any route
    }
}
