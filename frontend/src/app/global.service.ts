import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GlobalService {
  userDetails:any;
  constructor() {
    this.userDetails = {}
  }

  setUserDetails(user:any) {
    this.userDetails = user
  }

  getUserDetails() {
    return this.userDetails;
  }
}
