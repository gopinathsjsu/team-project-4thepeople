import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { SignupService } from './signup.service';


interface formDataInterface {
  "username": string;
  "first_name": string;
  "last_name": string;
  "email": string;
  "password1": string;
  "password2": string;

};
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  username: string = '';
  first_name: string = '';
  last_name: string = '';
  email: string = '';
  password1: string = '';
  password2: string = '';
  comparedPasswordBoolean:boolean = true;

  constructor(private service: SignupService) { }

  ngOnInit(): void {
  }

  onSignup(form: NgForm) {
    if (form.valid) {

      let formData: formDataInterface = {
        "username": this.username,
        "first_name": this.first_name,
        "last_name": this.last_name,
        "email": this.email,
        "password1": this.password1,
        "password2": this.password2
      }

      this.service.signUpService(formData)
      .subscribe(response => {
        console.log(response);
      })
    }
  }

  comparePasswords() {
    if(this.password1 == this.password2) {
      this.comparedPasswordBoolean = true
    } else {
      this.comparedPasswordBoolean = false
    }
  }
}
