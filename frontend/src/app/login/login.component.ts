import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { LoginService } from './login.service';
import { GlobalService } from '../global.service';
import { transpileModule } from 'typescript';
interface formDataInterface {
  "username": string;
  "password": string;

};
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username: string = '';
  password: string = '';
  unauthorized: string = '';
  userDetails:Object={};
  constructor(private router: Router, private service: LoginService, private globalService: GlobalService) { }

  ngOnInit(): void {
  }
  onLogin(form:NgForm) {
    if (form.valid) {

      let formData: formDataInterface = {
        "username": this.username,
        "password": this.password
      }

      this.service.loginService(formData)
      .subscribe(response => {
        let resSTR = JSON.stringify(response);
        let resJSON = JSON.parse(resSTR);
        this.userDetails = {
          'username': resJSON.data.username,
          'first_name': resJSON.data.first_name,
          'last_name': resJSON.data.last_name,
          'email': resJSON.data.email,
          'isLogged': true
        }
        localStorage.setItem('username', resJSON.data.username)
        localStorage.setItem('first_name', resJSON.data.first_name)
        localStorage.setItem('last_name', resJSON.data.last_name)
        localStorage.setItem('email', resJSON.data.email)
        localStorage.setItem('isLogged', 'true');
        this.globalService.setUserDetails(this.userDetails);
        this.router.navigate([""])
      }, error => {
        this.unauthorized = 'Please enter correct username and password'
      })
    }
  }
  signup() {
    this.router.navigate(["signup"])
  }
}
