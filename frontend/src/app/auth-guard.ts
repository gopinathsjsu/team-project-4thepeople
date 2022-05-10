import { Injectable } from '@angular/core';
import { Router, CanActivate, RouterStateSnapshot, ActivatedRouteSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service'
@Injectable()
export class AuthGuard implements CanActivate {

    constructor(private router: Router
        , private authService: AuthService) {}

    // canActivate(next: ActivatedRouteSnapshot,
    //     state: RouterStateSnapshot) {
    //     // Check to see if a user has a valid token
    //     let url: string = state.url;
    //     return this.checkLogin(url);
        
        
    // }
    canActivate(route: ActivatedRouteSnapshot,state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
        let isAuth = this.authService.isLoggedIn()
        if(!isAuth) {
          this.router.navigate(['home'])
        }
        return isAuth;
      }

}