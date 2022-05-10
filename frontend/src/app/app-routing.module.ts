import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RoomsComponent } from './rooms/rooms.component';
import { SignupComponent } from './signup/signup.component';
import { ReservationComponent } from './reservation/reservation.component';
import { RewardsComponent } from './rewards/rewards.component';
import { BookingsComponent } from './bookings/bookings.component';
import { AuthGuard } from './auth-guard';

const routes: Routes = [
  
  {path:'home',component:HomeComponent},
  {path:'login',component:LoginComponent},  
  {path:'signup',component:SignupComponent},
  {path:'rooms',component:RoomsComponent},
  {path:'reservation',component:ReservationComponent, canActivate: [AuthGuard] },
  {path:'rewards', component:RewardsComponent, canActivate: [AuthGuard] },
  {path:'bookings',component:BookingsComponent, canActivate: [AuthGuard] },
  {path:'**', redirectTo:'home'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
