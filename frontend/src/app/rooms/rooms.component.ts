import { Component, NgZone, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { GlobalService } from '../global.service';
import { NavigationStart, Event as NavigationEvent } from '@angular/router';
import * as _ from 'lodash'

@Component({
  selector: 'app-rooms',
  templateUrl: './rooms.component.html',
  styleUrls: ['./rooms.component.css']
})
export class RoomsComponent implements OnInit {
  roomDetails: any;
  groupByTypeDeluxe:any;
  groupByTypeDeluxeByLocation:any;
  locationsDeluxe:any;
  constructor(private globalService: GlobalService, private router: Router, private zone:NgZone) {
  }

  ngOnInit(): void {
    this.roomDetails = localStorage.getItem("response");
    this.roomDetails = JSON.parse(this.roomDetails)
    this.roomDetails = Object.values(this.roomDetails)
    this.groupByTypeDeluxe = _.filter(this.roomDetails, {'room_type': 'Deluxe'})
    this.groupByTypeDeluxeByLocation = _.chain(this.groupByTypeDeluxe)
    .groupBy("room_location")
    .map((value, key) => ({ room_location: key, rooms: value }))
    .value()
    this.locationsDeluxe = [...new Set(this.groupByTypeDeluxe.map((item: { room_location: any; }) => item.room_location))]
  }

}
