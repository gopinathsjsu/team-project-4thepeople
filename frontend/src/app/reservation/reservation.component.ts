import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NavigationStart, Event as NavigationEvent } from '@angular/router';
import { GlobalService } from '../global.service';
import { IDropdownSettings } from 'ng-multiselect-dropdown';
import { MatStartDate } from '@angular/material/datepicker';
import * as _ from 'lodash'
import * as moment from 'moment';
import { FormControl, NgForm } from '@angular/forms';
import { ReservationService } from './reservation.service';
import { SearchService } from '../home/search.service';

interface formDataInterface {
  "room_no": any;
  "number_of_guests": any;
  "start_day": Date;
  "end_day": Date;
  "booking_amenities": any;
  "room_price": any,
  "username": string;
  "reward_points": any;
  "booking_location": any;
  "booking_room_type": any;
};

interface emailFormDataInterface {
  "room_no": any;
  "number_of_guests": any;
  "start_day": Date;
  "end_day": Date;
  "room_price": any,
  "username": string;
  "email": any;
  "booking_location": any;
};
interface roomDataInterface {
  "username": any;
  "room_no": any;
  "number_of_guests": any;
  "booking_amenities": any;
  "start_day": any;
  "end_day": any;
  "room_price": any;
}


@Component({
  selector: 'app-reservation',
  templateUrl: './reservation.component.html',
  styleUrls: ['./reservation.component.css']
})

export class ReservationComponent implements OnInit {

  title = 'frontend';
  isLoggedIn: boolean = false;
  userDetails: any;
  openDropdownVal: boolean = false;
  room_details: any;
  value = 0;
  room_price: any;
  number_of_guests: number = 1;
  first_name: any;
  last_name: any;
  email: any;
  username: any;
  rooms = 1;
  minDate: Date;
  disable_start: boolean = false;
  minDate1: Date;
  maxEnd: Date;
  start_day: any;
  end_day: any;
  room_type: any;
  dropdownList = [
    'Studio', 'Suite', 'Deluxe'
  ];
  selectedItems: string[] = [];
  dropdownSettings: IDropdownSettings = {
    singleSelection: false,
    selectAllText: 'Select All',
    unSelectAllText: 'UnSelect All',
    itemsShowLimit: 3,
    allowSearchFilter: true
  };
  dropdownSettingsRoom: IDropdownSettings = {
    singleSelection: true,
    itemsShowLimit: 3,
    allowSearchFilter: true
  };

  dropdownList1 = [
    'Daily Continental Breakfast',
    'Access to fitness room',
    'Access to Swimming Pool and Jacuzzi',
    'Daily Parking',
    'All meals included']
  selectedItems1: string[] = [];
  amenities_cost: number = 0;
  successbooking: boolean = false;
  guestscap: number = 0;
  number_of_days: number = 1;
  room_number: any;
  base_price: any;
  modify: string = 'Reserve';
  successmodification: boolean = false;
  modifiedAmount: any;
  modifiedAbs: any;
  totalrooms: any;
  matching_rooms: any;
  foundRoomDetails: any;
  originalguestcap: number = 0;
  totalAmenities: number = 0;
  totalBooking: number = 0;
  bookingerror: boolean = false;

  constructor(private router: Router, private reservationService: ReservationService, private homeService: SearchService) {
    this.minDate = new Date();
    this.minDate1 = new Date();
    this.maxEnd = new Date();
    this.minDate1.setDate(this.minDate1.getDate() + 1)
  }
  ngOnInit(): void {
    this.first_name = localStorage.getItem('first_name')
    this.last_name = localStorage.getItem('last_name')
    this.email = localStorage.getItem('email')
    this.username = localStorage.getItem('username')
    this.selectedItems = []
    if (localStorage.getItem('room_details')) {
      this.room_details = localStorage.getItem('room_details')
      this.totalrooms = localStorage.getItem('roomcount')
      this.foundRoomDetails = localStorage.getItem('allRoomsMatch')
      this.foundRoomDetails = JSON.parse(this.foundRoomDetails)
      this.room_details = JSON.parse(this.room_details)
      this.room_price = this.room_details.price
      this.room_type = this.room_details.room_type
      this.room_number = this.room_details.room_no
      if (this.room_type == 'Studio') {
        this.guestscap = 2;
        this.originalguestcap = 2;
      } else if (this.room_type == 'Suite') {
        this.guestscap = 4;
        this.originalguestcap = 4;
      } else if (this.room_type == 'Deluxe') {
        this.guestscap = 6;
        this.originalguestcap = 6;
      }
      this.selectedItems.push(this.room_type)
      let dateString: any = localStorage.getItem('roomstartsearch')
      this.start_day = new Date(dateString)
      this.disable_start = true
      let date = new Date()
      date = this.start_day
      this.minDate1.setDate(date.getDate() + 1)
      this.maxEnd.setDate(date.getDate() + 7)
    } else if (localStorage.getItem('reservationDetails')) {
      this.modify = 'Modify'
      this.room_details = localStorage.getItem('reservationDetails')
      this.room_details = JSON.parse(this.room_details)
      this.room_details = this.room_details
      this.room_price = this.room_details.total_amount
      this.room_type = this.room_details.room_type
      if (this.room_type == 'Studio') {
        this.guestscap = 2;
      } else if (this.room_type == 'Suite') {
        this.guestscap = 4;
      } else if (this.room_type == 'Deluxe') {
        this.guestscap = 6;
      }
      this.number_of_guests = this.room_details.guests
      this.selectedItems.push(this.room_details.room_type)
      this.start_day = new Date(this.room_details.start_day)
      this.end_day = new Date(this.room_details.end_day)
      let date = new Date()
      date = this.start_day
      this.minDate1.setDate(date.getDate() + 1)
      this.maxEnd.setDate(date.getDate() + 7)
      this.selectedItems1 = this.room_details.amenities
      this.room_details.price = this.room_details.total_amount
      this.base_price = this.room_details.total_amount
      _.forEach(this.room_details.amenities, val => {
        if (val == 'Daily Continental Breakfast') {
          this.base_price = this.base_price - 50;
          this.amenities_cost = this.amenities_cost + 50
        }
        else if (val == 'Access to fitness room') {
          this.base_price = this.base_price - 50;
          this.amenities_cost = this.amenities_cost + 50
        }
        else if (val == 'Access to Swimming Pool and Jacuzzi') {
          this.base_price = this.base_price - 50;
          this.amenities_cost = this.amenities_cost + 50
        }
        else if (val == 'Daily Parking') {
          this.base_price = this.base_price;
        }
        else if (val == 'All meals included') {
          this.base_price = this.base_price - 150;
          this.amenities_cost = this.amenities_cost + 150
        }
      })
    }
  }

  onItemSelect(item: any) {
    if (item == 'Daily Continental Breakfast') {
      this.room_price = this.room_price + (50 * this.rooms);
      this.amenities_cost = this.amenities_cost + (50 * this.rooms)
      this.totalAmenities++
    }
    else if (item == 'Access to fitness room') {
      this.room_price = this.room_price + (50 * this.rooms);
      this.amenities_cost = this.amenities_cost + (50 * this.rooms)
      this.totalAmenities++
    }
    else if (item == 'Access to Swimming Pool and Jacuzzi') {
      this.room_price = this.room_price + (50 * this.rooms);
      this.amenities_cost = this.amenities_cost + (50 * this.rooms)
      this.totalAmenities++
    }
    else if (item == 'Daily Parking') {
      this.room_price = this.room_price;
      this.amenities_cost = this.amenities_cost;
    }
    else if (item == 'All meals included') {
      this.room_price = this.room_price + (150 * this.rooms);
      this.amenities_cost = this.amenities_cost + (150 * this.rooms);
      this.totalAmenities++
    }
  }
  onSelectAll(items: any) {
    this.totalAmenities = 4
    this.room_price = this.room_price + (300 * this.rooms);
    this.amenities_cost = this.amenities_cost + (300 * this.rooms)
  }

  onDeSelectAll(items: any) {
    this.selectedItems1 = []
    this.totalAmenities = 0
    this.room_price = this.room_details.price;
    this.amenities_cost = this.amenities_cost
  }

  onVendorDeSelect(item: any) {
    if (item == 'Daily Continental Breakfast') {
      this.room_price = this.room_price - (50 * this.rooms);
      this.amenities_cost = this.amenities_cost - (50 * this.rooms)
      this.totalAmenities--
    }
    else if (item == 'Access to fitness room') {
      this.room_price = this.room_price - (50 * this.rooms);
      this.amenities_cost = this.amenities_cost - (50 * this.rooms)
      this.totalAmenities--
    }
    else if (item == 'Access to Swimming Pool and Jacuzzi') {
      this.room_price = this.room_price - (50 * this.rooms);
      this.amenities_cost = this.amenities_cost - (50 * this.rooms)
      this.totalAmenities--
    }
    else if (item == 'Daily Parking') {
      this.room_price = this.room_price;
      this.amenities_cost = this.amenities_cost
    }
    else if (item == 'All meals included') {
      this.room_price = this.room_price - (150 * this.rooms);
      this.amenities_cost = this.amenities_cost - (150 * this.rooms)
      this.totalAmenities--
    }
  }

  OnGuestSelect() {
    this.room_price = this.room_details.price
    if (this.room_details.guests) {
      if (this.room_details.guests > this.number_of_guests) {
        this.room_price = this.room_price * this.rooms * this.number_of_guests * this.number_of_days - this.amenities_cost
        this.room_price = this.room_price / this.number_of_guests
      } else {
        this.room_price = this.room_price * this.rooms * this.number_of_guests * this.number_of_days + this.amenities_cost
      }
    } else {
      this.room_price = this.room_details.price
      if (this.room_details.guests > this.number_of_guests) {
        this.room_price = this.room_price * this.rooms * this.number_of_guests * this.number_of_days - this.amenities_cost
        this.room_price = this.room_price - this.number_of_guests * this.room_details.price
      } else {
        this.room_price = this.room_price * this.rooms * this.number_of_guests * this.number_of_days + this.amenities_cost
      }
      this.room_price = this.room_price * this.rooms * this.number_of_guests * this.number_of_days + this.amenities_cost
    }

  }

  onReservation(form: NgForm) {
    if (form.valid) {
      if (this.modify == 'Reserve') {
        if (this.rooms > 1) {
          let amenities = this.amenities_cost / this.totalAmenities
          amenities = amenities / this.rooms
          let total_cost = this.room_price / this.rooms
          total_cost = total_cost / this.number_of_guests + amenities
          let guests = this.number_of_guests / this.rooms
          for (let i = 0; i < this.rooms; i++) {
            this.start_day = moment(this.start_day).format('YYYY-MM-DD')
            this.end_day = moment(this.end_day).format('YYYY-MM-DD')
            let formData: formDataInterface = {
              "username": this.username,
              "room_no": this.foundRoomDetails[i].room_no,
              "number_of_guests": guests.toString(),
              "booking_amenities": this.selectedItems1.toString(),
              "start_day": this.start_day.toString(),
              "end_day": this.end_day.toString(),
              "room_price": total_cost.toString(),
              "reward_points": 50,
              "booking_location": this.room_details.room_location,
              "booking_room_type": this.room_details.room_type
            }
            this.reservationService.reservationServiceCall(formData)
              .subscribe(response => {
                this.successbooking = true;
                this.reservationService.callRewards(formData)
                  .subscribe(response => {
                    console.log(response)
                  })
              })
          }
        } else {
          this.start_day = moment(this.start_day).format('YYYY-MM-DD')
          this.end_day = moment(this.end_day).format('YYYY-MM-DD')
          let formData: formDataInterface = {
            "username": this.username,
            "room_no": this.room_details.room_no,
            "number_of_guests": this.number_of_guests.toString(),
            "booking_amenities": this.selectedItems1.toString(),
            "start_day": this.start_day.toString(),
            "end_day": this.end_day.toString(),
            "room_price": this.room_price.toString(),
            "reward_points": 50,
            "booking_location": this.room_details.room_location,
            "booking_room_type": this.room_details.room_type
          }

          let emailFormData: emailFormDataInterface = {
            "username": this.username,
            "room_no": this.room_details.room_no,
            "number_of_guests": this.number_of_guests.toString(),
            "start_day": this.start_day.toString(),
            "end_day": this.end_day.toString(),
            "room_price": this.room_price.toString(),
            "booking_location": this.room_details.room_location,
            "email": this.email
          }
          this.reservationService.reservationServiceCall(formData)
            .subscribe(response => {
              this.successbooking = true;
              this.reservationService.callRewards(formData)
                .subscribe(response => {
                  console.log(response)
                })
              this.reservationService.sendEmail(emailFormData)
                .subscribe(response => {
                  console.log(response)
                })
            }, error => {
              this.bookingerror = true;
            })
        }
      } else if (this.modify == 'Modify') {
        this.start_day = moment(this.start_day).format('YYYY-MM-DD')
        this.end_day = moment(this.end_day).format('YYYY-MM-DD')
        let formData: roomDataInterface = {
          "username": this.username,
          "room_no": this.room_details.room_no,
          "number_of_guests": this.number_of_guests.toString(),
          "booking_amenities": this.selectedItems1.toString(),
          "start_day": this.start_day.toString(),
          "end_day": this.end_day.toString(),
          "room_price": this.room_price.toString()
        }
        this.reservationService.modifyData(formData)
          .subscribe(response => {
            this.successmodification = true;
            this.modifiedAmount = this.room_price - this.room_details.total_amount
            this.modifiedAbs = Math.abs(this.modifiedAmount)
          })
      }
    }
  }
  startDateChange() {
    let day = new Date()
    day = this.start_day
    this.minDate1.setDate(day.getDate() + 1)
    this.start_day = moment(this.start_day).format('YYYY-MM-DD')
    this.homeService.searchService(this.start_day)
      .subscribe(response => {
        let resSTR = JSON.stringify(response);
        let resJSON = JSON.parse(resSTR);
        this.room_details = _.find(resJSON.data, { 'room_no': this.room_number })
        if (this.room_details) this.room_price = this.room_details.price
      })

  }
  closeModal() {
    this.successbooking = false
    this.router.navigate(["bookings"])
  }

  calculateDiff(sentDate: any) {
    var date1: any = new Date(sentDate);
    var startDate: any = new Date(this.start_day)
    var diffDays: any = Math.floor((date1 - startDate) / (1000 * 60 * 60 * 24));
    this.number_of_days = diffDays
    if (this.number_of_days <= 0) {
      this.number_of_days = 1
    } else {
      this.number_of_days = this.number_of_days + 1
    }
    if (localStorage.getItem('room_details')) {
      this.room_details = localStorage.getItem('room_details')
      this.room_details = JSON.parse(this.room_details)
      this.room_price = this.room_details.price
    }
    else if (localStorage.getItem('reservationDetails')) {
      this.room_details = localStorage.getItem('reservationDetails')
      this.room_details = JSON.parse(this.room_details)
      this.room_price = this.room_details.total_amount
    }

    this.room_price = this.room_price * this.rooms * this.number_of_guests * this.number_of_days + this.amenities_cost
  }
  closeModalModify() {
    this.successmodification = false
    this.router.navigate(["bookings"])
  }
  closeModalBooking() {
    this.bookingerror = false
  }

  redirectToHome() {
    this.router.navigate([""])
  }
  increaseGuestCap() {
    this.guestscap = this.rooms * this.originalguestcap
    this.room_price = this.room_details.price
    this.room_price = this.room_price * this.rooms * this.number_of_guests * this.number_of_days + this.amenities_cost
  }
}
