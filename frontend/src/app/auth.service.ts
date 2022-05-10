import { Injectable } from '@angular/core';
import { Router,NavigationStart, Event as NavigationEvent } from '@angular/router';
import { Location } from '@angular/common';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isLoggedIn(): boolean {
    var isAuth = false;
    if(localStorage.getItem('isLogged')) isAuth = true;
    return isAuth;
  }
 
  returnValue: any
  constructor(private router: Router, location: Location) {
    
    
  }
  isAuthenticated(url: string) {
    let token = localStorage.getItem('role');
    token = '/'+token
    if (token === url) return true
    else if (url === '/signup') return true
    return false
  }
}