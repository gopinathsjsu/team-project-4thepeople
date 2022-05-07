import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Form } from '@angular/forms';
@Injectable({
  providedIn: 'root'
})
export class SignupService {

  constructor(private httpClient: HttpClient) {}

  signUpService(form: any) {
    const formData = new FormData();
    formData.append('email', form['email']);
    formData.append('username', form['username']);
    formData.append('first_name', form['first_name']);
    formData.append('last_name', form['last_name']);
    formData.append('password1', form['password1']);
    formData.append('password2', form['password2']);
    return this.httpClient.post('http://sw-engineering-system.herokuapp.com/accounts/api/register/', formData);
  }
}
