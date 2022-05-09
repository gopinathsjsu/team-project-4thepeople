import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GlobalService {
  userDetails:any;
  roomDetails:any;
  constructor() {
    this.userDetails = {}
  }

  setUserDetails(user:any) {
    this.userDetails = user
  }

  getUserDetails() {
    return this.userDetails;
  }

  getRoomDetails() {
    return this.roomDetails;
  }

  setRoomDetails(room:any) {
    this.roomDetails = room
  }
}
