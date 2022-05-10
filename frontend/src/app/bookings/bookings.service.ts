import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class BookingsService {

  constructor(private httpClient:HttpClient) { }

  getBookingsForUser(username:any) {
    let form = new FormData();
    form.append('username', username);
    return this.httpClient.post('https://sw-engineering-system.herokuapp.com/api/booking_details/', form);
  }

  deleteBooking(username:any, room_no:any) {
    let form = new FormData();
    form.append('username', username)
    form.append('room_no', room_no)

    return this.httpClient.delete('http://sw-engineering-system.herokuapp.com/api/booking/',{body: form})
  }

  
  delRewards(formData: any) {
    const formReq = new FormData();
    formReq.append('username', formData['username'])
    formReq.append('reward_points', formData['reward_points'])

    return this.httpClient.delete('https://sw-engineering-system.herokuapp.com/accounts/api/manage_account/', {body:formReq})
  }

}
