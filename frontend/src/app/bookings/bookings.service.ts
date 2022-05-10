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
}
