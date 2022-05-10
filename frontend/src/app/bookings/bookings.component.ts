import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { BookingsService } from './bookings.service';
import * as _ from 'lodash'
import * as moment from 'moment';

@Component({
  selector: 'app-bookings',
  templateUrl: './bookings.component.html',
  styleUrls: ['./bookings.component.css']
})
export class BookingsComponent implements OnInit {
  username: any;
  first_name:any;
  last_name:any;
  deletion:boolean=false;
  deletedRoom:any;
  constructor(private router:Router, private bookingService: BookingsService) { }

  ngOnInit(): void {
    this.username = localStorage.getItem('username');
    this.first_name = localStorage.getItem('first_name')
    this.last_name = localStorage.getItem('last_name')
    this.getAllOwners()
  }

  public displayedColumns: string[] = ['first_name', 'last_name', 'guests', 'room_no', 'room_type', 'start_day', 'end_day', 'room_location', 'total_amount', 'amenities', 'booked_date', 'update', 'delete'];
  public dataSource = new MatTableDataSource();

  closeModal() {
    this.deletion = false;
    location.reload()
  }

  public getAllOwners = () => {
    this.bookingService.getBookingsForUser(this.username)
    .subscribe(response => {
      let resSTR = JSON.stringify(response);
      let resJSON = JSON.parse(resSTR);
      let values = _.values(resJSON.data)
      _.forEach(values, val=> {
        val.first_name = this.first_name
        val.last_name = this.last_name
        val.booked_date = moment(val.booked_date).format('YYYY-MM-DD');
      })
      this.dataSource.data = values
    })
    this.dataSource.data = [
    ]
  }
  public redirectToUpdate = () => {
    localStorage.removeItem('room_details')
    localStorage.setItem('reservationDetails', JSON.stringify(this.dataSource.data))
    this.router.navigate(["reservation"])
  }
  public redirectToDelete = (roomno: string) => {
    this.bookingService.deleteBooking(this.username, roomno)
    .subscribe(response=>{
      this.deletion = true
      this.deletedRoom = _.find(this.dataSource.data, {'room_no': roomno})
    })
  }

}
