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
    return this.httpClient.post('https://sw-engineering-system.herokuapp.com/accounts/api/register/', form);
  }
}
