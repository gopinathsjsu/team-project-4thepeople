import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Form } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class ReservationService {

  constructor(private httpClient: HttpClient) { }

  reservationService(form: any) {
    return this.httpClient.get('https://sw-engineering-system.herokuapp.com/booking/api/rooms/', form);
  }
}
