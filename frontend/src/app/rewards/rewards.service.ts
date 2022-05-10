import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RewardsService {

  constructor(private httpClient: HttpClient) { }

  getRewards(username:any) {
    let formData = new FormData();
    formData.append('username', username)
    return this.httpClient.post('https://sw-engineering-system.herokuapp.com/accounts/api/profile/', formData)
  }
}
