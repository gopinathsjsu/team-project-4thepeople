import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NavigationStart, Event as NavigationEvent } from '@angular/router';
import { GlobalService } from '../global.service';
import { IDropdownSettings } from 'ng-multiselect-dropdown';

// interface ReservationInterface {
//   "first_name": string;
//   "last_name": string;
//   "email": string;
//   "room_no" : number
// };

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

  first_name:any;
  last_name: any;
  email: any;

  constructor(private router: Router, private globalService: GlobalService) {
    let urlRoute = this.router.events.subscribe(
      (event: NavigationEvent) => {
        if (event instanceof NavigationStart) {
          if ('/reservation' === event.url) {
              // this.isLoggedIn = true
              this.userDetails = this.globalService.getUserDetails()
              this.first_name = localStorage.getItem(this.first_name)
              // this.last_name = this.userDetails.last_name
              this.last_name = localStorage.getItem(this.last_name)
              // this.email = this.userDetails.email
              this.email = localStorage.getItem(this.email)
          }
        }
      })
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
      { item_id: 1, item_text: 'Continental Breakfast' },
      { item_id: 2, item_text: 'meals' },
      { item_id: 3, item_text: 'Jacuzzi' },
      { item_id: 4, item_text: 'parking' }];
    selectedItems1 = [
      { item_id: 1, item_text: 'Continental Breakfast' }
    ];

  ngOnInit(): void{

  }
  redirecttoHome() {
    this.router.navigate(["home"])
  }

    value = 0;
    
    onItemSelect(item: any) {
      console.log(item);
    }
    onSelectAll(items: any) {
      console.log(items);
    }
  
}
