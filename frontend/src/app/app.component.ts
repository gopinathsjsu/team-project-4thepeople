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
            if(localStorage.getItem('isLogged')=='true') {
              this.isLoggedIn = true
              this.userDetails = {
                'username': localStorage.getItem('username'),
                'first_name': localStorage.getItem('first_name'),
                'last_name': localStorage.getItem('last_name'),
                'email': localStorage.getItem('email')
              }
            } else {
              this.isLoggedIn = false
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
    localStorage.clear()
    this.router.navigate(["home"])
    location.reload()
  }
  bookings() {
    this.router.navigate(["bookings"])
  }

  rewards() {
    this.router.navigate(["rewards"])
  }

  redirectToHome() {
    this.router.navigate(["home"])
  }
}
