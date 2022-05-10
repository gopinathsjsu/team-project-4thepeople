import { Component, OnInit } from '@angular/core';
import { RewardsService } from './rewards.service';

@Component({
  selector: 'app-rewards',
  templateUrl: './rewards.component.html',
  styleUrls: ['./rewards.component.css']
})
export class RewardsComponent implements OnInit {
  username:any;
  level:any;
  reward_points:any;
  constructor(private rewardsService: RewardsService) { }

  ngOnInit(): void {
    this.username = localStorage.getItem('username');
    this.rewardsService.getRewards(this.username)
    .subscribe(response => {
      let resSTR = JSON.stringify(response);
      let resJSON = JSON.parse(resSTR);
      this.level = resJSON.data.level
      this.reward_points = resJSON.data.total_reward_points
    })
  }

}
