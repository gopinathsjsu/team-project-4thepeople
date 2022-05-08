import { Component, NgZone, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { GlobalService } from '../global.service';
import { NavigationStart, Event as NavigationEvent } from '@angular/router';
import * as _ from 'lodash'
import { IDropdownSettings } from 'ng-multiselect-dropdown';

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
  dropdownList = <any>[];
  selectedItems = <any>[];
  groupByTypeDeluxeUpdated:any;
  groupByTypeStudios:any;
  groupByTypeStudiosByLocation:any;
  locationsStudios:any;
  dropdownListStudios = <any>[];
  selectedItemsStudios = <any>[];
  groupByTypeStudiosUpdated:any;
  groupByTypeSuite:any;
  groupByTypeSuiteByLocation:any;
  locationsSuite:any;
  dropdownListSuite = <any>[];
  selectedItemsSuite = <any>[];
  groupByTypeSuiteUpdated:any;
  noDropdown:boolean=false;
  locationValue:any='';
  dropdownSettings:IDropdownSettings = {
    singleSelection: true,
    itemsShowLimit: 5,
    allowSearchFilter: true
  };
  
  constructor(private globalService: GlobalService, private router: Router, private zone:NgZone) {
  }

  ngOnInit(): void {
    this.roomDetails = localStorage.getItem("response");
    this.roomDetails = JSON.parse(this.roomDetails)
    this.roomDetails = Object.values(this.roomDetails)
    this.groupByTypeDeluxe = _.filter(this.roomDetails, {'room_type': 'Deluxe'})
    this.dropdownList = [...new Set(this.groupByTypeDeluxe.map((item: { room_location: any; }) => item.room_location))]
    this.groupByTypeStudios = _.filter(this.roomDetails, {'room_type': 'Studio'})
    this.dropdownListStudios = [...new Set(this.groupByTypeStudios.map((item: { room_location: any; }) => item.room_location))]
    this.groupByTypeSuite = _.filter(this.roomDetails, {'room_type': 'Suite'})
    this.dropdownListSuite = [...new Set(this.groupByTypeSuite.map((item: { room_location: any; }) => item.room_location))]
    this.locationValue = localStorage.getItem('location')
    if(this.locationValue) {
      this.groupByTypeDeluxeUpdated = [...this.groupByTypeDeluxe]
      this.groupByTypeStudiosUpdated = this.groupByTypeStudios
      this.groupByTypeSuiteUpdated = this.groupByTypeSuite
      this.noDropdown = true
    }
  }
  changeData() {
    this.groupByTypeDeluxeUpdated = _.filter(this.groupByTypeDeluxe, {'room_location': this.selectedItems[0]})
    this.groupByTypeStudiosUpdated = _.filter(this.groupByTypeStudios, {'room_location': this.selectedItemsStudios[0]})
    this.groupByTypeSuiteUpdated = _.filter(this.groupByTypeSuite, {'room_location': this.selectedItemsSuite[0]})
  }
}
