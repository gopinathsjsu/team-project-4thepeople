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
}
