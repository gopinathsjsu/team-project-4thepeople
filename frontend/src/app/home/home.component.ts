import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Options, LabelType } from 'ng5-slider';
import { FormControl, FormGroup } from '@angular/forms';
import { SearchService } from './search.service';
import { DatePipe } from '@angular/common';
import * as moment from 'moment';
import { GlobalService } from '../global.service';
import { IDropdownSettings } from 'ng-multiselect-dropdown';
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
  dropdownSettings:IDropdownSettings = {
    singleSelection: true,
    itemsShowLimit: 5,
    allowSearchFilter: true
  };
  dropdownList = ["Albany", "Ann Arbor",
  "Arlington", "Athens",
  "Atlanta", "Atlantic City",
  "Austin", "Bakersfield", "Baltimore",
  "Bellevue", "Berkeley", "Birmingham", "Bloomington",
  "Boulder", "Buffalo",
  "Burlington", "Cambridge",
  "Champaign", "Charlotte",
  "Chicago", "Cincinnati", "Clarksville", "Cleveland",
  "Colorado Springs", "Columbia",
  "Dallas",
  "Dayton", "Denver", "Detroit",
  "Durham",
  "Fairfield", "Fargo",
  "Fremont",
  "Fresno", "Fullerton", "Gainesville",
  "Hollywood",
  "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence",
  "Irvine", "Jersey City",
  "Kansas City",
  "Lakewood",
  "Las Vegas",
  "Long Beach", "Los Angeles",
  "New York", "New York City", "Newark", "Oakland",
  "Portland", "Raleigh",
  "Riverside", "Sacramento", "San Diego", "San Francisco", "San Jose", "Santa Barbara", "Santa Clara",
  "Santa Clarita", "Santa Cruz", "Sunnyvale", "Syracuse",
  "Tampa", "Tucson", "Washington",
  "Waterloo"]
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
    if(this.dateRange.value.start){
      this.start_date = this.dateRange.value.start
      this.start_date = moment(this.start_date).format('YYYY-MM-DD');
    }
    else {
      this.start_date =  moment().format('YYYY-MM-DD');
    }
    let formData: formDataInterface = {
      "location": this.location,
      "start_date": this.start_date,
      "price_end": this.maxValue,
      "price_start": this.minValue
    }
    let empty: any;
    this.globalService.setRoomDetails(empty)
    localStorage.setItem('location', this.location)
   this.searchService.searchServiceCall(formData)
   .subscribe(response => {
    let resSTR = JSON.stringify(response);
    let resJSON = JSON.parse(resSTR);
    localStorage.setItem('response', JSON.stringify(resJSON.data));
    this.router.navigate(["rooms"])
   }) 
  }
  
}
