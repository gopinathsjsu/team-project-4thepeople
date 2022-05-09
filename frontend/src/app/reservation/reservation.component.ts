import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NavigationStart, Event as NavigationEvent } from '@angular/router';
import { GlobalService } from '../global.service';
import { IDropdownSettings } from 'ng-multiselect-dropdown';
import { MatStartDate } from '@angular/material/datepicker';
import * as _ from 'lodash'
import { FormControl } from '@angular/forms';

interface ReservationInterface {
  "first_name": string;
  "last_name": string;
  "email": string;
  "roomno" : number;
  "guests" : number;
  "arrival" : Date;
  "departure" : Date;
  "roomtype" : any;
  "amenities" : any;
  "totalcost" :number

};

@Component({
  selector: 'app-reservation',
  templateUrl: './reservation.component.html',
  styleUrls: ['./reservation.component.css']
})
export class ReservationComponent implements OnInit {
  title = 'frontend';
  isLoggedIn:boolean = false;
  userDetails:any;
  openDropdownVal:boolean=false;

  guestnumber = 1;
  first_name:any;
  last_name: any;
  email: any;
  rooms = 1;
  minDate: Date;
  minDate1: Date;

  constructor(private router: Router, private globalService: GlobalService) {
    let urlRoute = this.router.events.subscribe(
      (event: NavigationEvent) => {
        if (event instanceof NavigationStart) {
          if ('/reservation' === event.url) {
              // this.isLoggedIn = true
              // this.userDetails = this.globalService.getUserDetails()
              this.first_name = localStorage.getItem(this.first_name)
              console.log(localStorage.getItem(this.first_name))
              // this.last_name = this.userDetails.last_name
              this.last_name = localStorage.getItem('last_name')
              console.log(this.last_name)
              // this.email = this.userDetails.email
              this.email = localStorage.getItem(this.email)
          }
        }
      })

      this.minDate = new Date();
      this.minDate1 = new Date();
      this.minDate1.setDate(this.minDate1.getDate() + 1);


   }
    dropdownList = [
      { item_id: 1, item_text: 'Classic' },
      { item_id: 2, item_text: 'Deluxe' },
      { item_id: 3, item_text: 'suite' }];
    selectedItems = [
      { item_id: 1, item_text: 'Classic' }
    ];
    dropdownSettings:IDropdownSettings = {
      singleSelection: false,
      idField: 'item_id',
      textField: 'item_text',
      selectAllText: 'Select All',
      unSelectAllText: 'UnSelect All',
      itemsShowLimit: 3,
      allowSearchFilter: true
    };

    dropdownList1 = [
      { item_id: 1, item_text: 'Daily Continental Breakfast' },
      { item_id: 2, item_text: 'Access to fitness room' },
      { item_id: 3, item_text: 'Access to Swimming Pool and Jacuzzi' },
      { item_id: 4, item_text: 'Daily Parking' },
      { item_id: 3, item_text: 'All meals included' }];
    selectedItems1 = [
    ];

  ngOnInit(): void{
    this.first_name = localStorage.getItem('first_name')
    this.last_name = localStorage.getItem('last_name')
    this.email = localStorage.getItem('email')

  }
  redirecttoHome() {
    this.router.navigate(["home"])
  }

    value = 0;
    totalcost = 0;
    
    onItemSelect(item: any) {
      if(item.item_text=='Daily Continental Breakfast'){
        this.totalcost = this.totalcost + 50;
      }
      else if(item.item_text=='Access to fitness room'){
        this.totalcost = this.totalcost + 50;
      }
      else if(item.item_text=='Access to Swimming Pool and Jacuzzi'){
        this.totalcost = this.totalcost + 50;
      }
      else if(item.item_text=='Daily Parking'){
        this.totalcost = this.totalcost;
      }
      else if(item.item_text=='All meals included'){
        this.totalcost = this.totalcost + 150;
      }

      console.log(this.totalcost)

    }
    onSelectAll(items: any) {
      console.log(items);
      this.totalcost = 300;
      console.log(this.totalcost)
    }

    onDeSelectAll(items: any) {
      this.selectedItems1 = []
      console.log(items);
      this.totalcost = 0;
      console.log(this.totalcost)
    } 

    onVendorDeSelect(item: any) {
      let found = _.find(this.selectedItems1, item)
      this.selectedItems = _.reject(this.selectedItems1, found)
      console.log(this.selectedItems1)
      if(item.item_text=='Daily Continental Breakfast'){
        this.totalcost = this.totalcost - 50;
      }
      else if(item.item_text=='Access to fitness room'){
        this.totalcost = this.totalcost - 50;
      }
      else if(item.item_text=='Access to Swimming Pool and Jacuzzi'){
        this.totalcost = this.totalcost - 50;
      }
      else if(item.item_text=='Daily Parking'){
        this.totalcost = this.totalcost;
      }
      else if(item.item_text=='All meals included'){
        this.totalcost = this.totalcost - 150;
      }
      console.log(this.totalcost)
      }

      OnGuestSelect(){
        console.log(this.guestnumber)
       this.totalcost = this.totalcost * this.guestnumber;
      }

      OnRoomSelect(){
        console.log(this.rooms)
       this.totalcost = this.totalcost * this.rooms;
      }
   
}
