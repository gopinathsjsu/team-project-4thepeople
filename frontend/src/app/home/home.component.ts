import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Options, LabelType } from 'ng5-slider';
import { FormControl, FormGroup } from '@angular/forms';
import { SearchService } from './search.service';
import { DatePipe } from '@angular/common';
import * as moment from 'moment';
import { GlobalService } from '../global.service';
interface formDataInterface {
  "location": string;
  "start_date": string;
  "price_start": number;
  "price_end": number;
};
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  minValue: number = 0;
  maxValue: number = 1000;
  minDate: Date;
  dateRange = new FormGroup({
    start: new FormControl(),
    end: new FormControl()
  });
  location:string = '';
  start_date: string = '';
  options: Options = {
    floor: 0,
    ceil: 1000,
    translate: (value: number, label: LabelType): string => {
      switch (label) {
        case LabelType.Low:
          return '<b>Min: $ ' + value;
        case LabelType.High:
          return '<b>Max: $ ' + value;
        default:
          return '$ ' + value;
      }
    }
  };
  constructor(private router: Router, private searchService:SearchService, private globalService: GlobalService) {
    this.minDate = new Date()
  }

  ngOnInit(): void {
  }
  redirect() {
    this.router.navigate(["login"])
  }
  search() {
    let self = this
    this.start_date = this.dateRange.value.start
    this.start_date = moment().format('YYYY-MM-DD');
    let formData: formDataInterface = {
      "location": this.location,
      "start_date": this.start_date,
      "price_end": this.maxValue,
      "price_start": this.minValue
    }
    let empty: any;
    this.globalService.setRoomDetails(empty)
   this.searchService.searchServiceCall(formData)
   .subscribe(response => {
    let resSTR = JSON.stringify(response);
    let resJSON = JSON.parse(resSTR);
    localStorage.setItem('response', JSON.stringify(resJSON.data));
    self.router.navigate(["rooms"])
    location.reload()
   }) 
  }
}
