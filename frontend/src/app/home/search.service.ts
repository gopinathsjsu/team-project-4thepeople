import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { NgForm } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private httpClient: HttpClient) { }

  searchServiceCall(form:any) {
    const formdata = new FormData();

    formdata.append('location', form['location']);
    formdata.append('start_date', form['start_date']);
    formdata.append('price_start', form['price_start']);
    formdata.append('price_end', form['price_end']);

    return this.httpClient.post('https://sw-engineering-system.herokuapp.com/api/search/', formdata);
  }
}
