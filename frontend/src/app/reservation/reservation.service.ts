import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Form } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class ReservationService {

  constructor(private httpClient: HttpClient) { }

  reservationServiceCall(form: any) {
    const formData = new FormData();
    formData.append('room_no', form['room_no'])
    formData.append('number_of_guests', form['number_of_guests'])
    formData.append('start_day', form['start_day'])
    formData.append('end_day', form['end_day'])
    formData.append('booking_amenities', form['booking_amenities'])
    formData.append('room_price', form['room_price'])
    formData.append('username', form['username'])
    formData.append('booking_location', form['booking_location'])
    formData.append('booking_room_type', form['booking_room_type'])
    
    return this.httpClient.post('http://sw-engineering-system.herokuapp.com/api/booking/', formData);
  }


  callRewards(formData: any) {
    const formReq = new FormData();
    formReq.append('username', formData['username'])
    formReq.append('reward_points', formData['reward_points'])

    return this.httpClient.post('https://sw-engineering-system.herokuapp.com/accounts/api/manage_account/', formReq)
  }

  modifyData(form: any) {
    const formData = new FormData();
    formData.append('room_no', form['room_no'])
    formData.append('number_of_guests', form['number_of_guests'])
    formData.append('start_day', form['start_day'])
    formData.append('end_day', form['end_day'])
    formData.append('booking_amenities', form['booking_amenities'])
    formData.append('room_price', form['room_price'])
    formData.append('username', form['username'])

    return this.httpClient.put('http://sw-engineering-system.herokuapp.com/api/booking/',formData)
  }

  sendEmail(form:any) {
    const formData = new FormData();
    formData.append('room_no', form['room_no'])
    formData.append('guest', form['number_of_guests'])
    formData.append('start_day', form['start_day'])
    formData.append('end_day', form['end_day'])
    formData.append('total_amount', form['room_price'])
    formData.append('username', form['username'])
    formData.append('mails', form['email'])
    formData.append('location', form['booking_location'])

    return this.httpClient.post('https://wfhgr06xua.execute-api.us-east-1.amazonaws.com/dev/mail/sendmail/', formData);
  }
}
