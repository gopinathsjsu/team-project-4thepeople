import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { GlobalService } from './global.service';
import { NavigationStart, Event as NavigationEvent } from '@angular/router';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  isLoggedIn:boolean = false;
  userDetails:any;
  openDropdownVal:boolean=false;
  constructor(private router: Router, private globalService: GlobalService) {
    let urlRoute = this.router.events.subscribe(
      (event: NavigationEvent) => {
        if (event instanceof NavigationStart) {
          if ('/home' === event.url) {
            if(this.globalService.getUserDetails().isLogged) {
              this.isLoggedIn = true
              this.userDetails = this.globalService.getUserDetails()
            } else if(localStorage.getItem('isLogged')=='true') {
              this.isLoggedIn = true
            } else {
              this.isLoggedIn = false
            }
          }
        }
      })
  }
  ngOnInit():void {
    
  }

  redirect() {
    this.router.navigate(["login"])
  }
  redirectRooms() {
    this.router.navigate(["rooms"])
  }
  redirectToReserve() {
    this.router.navigate(["reservation"])
  }
  openDropdown() {
    this.openDropdownVal = !this.openDropdownVal
  }
  logout() {
    let userDetails = {}
    this.globalService.setUserDetails(userDetails)
    localStorage.setItem('username', '')
    localStorage.setItem('first_name', '')
    localStorage.setItem('last_name', '')
    localStorage.setItem('email', '')
    localStorage.setItem('isLogged', '')
    location.reload()
  }
}
