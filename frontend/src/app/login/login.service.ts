import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private httpClient: HttpClient) { }

  loginService(form: any) {
    const formData = new FormData();
    formData.append('username', form['username']);
    formData.append('password', form['password']);
    return this.httpClient.post('http://sw-engineering-system.herokuapp.com/accounts/api/signin/', formData);
  }
}
