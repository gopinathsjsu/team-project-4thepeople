from django.urls import path
from . import views
from .views import UsersRegistrationAPI, UsersSigninAPI, ManageHotelAccountView, UsersProfileAPI

urlpatterns = [
    path('user/', views.userPage, name="user-page"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    # bookings
    path('', views.home, name="home"),
    path('bookings/', views.bookings_list, name="booking_list"),
    path('bookings/create/', views.create_booking, name='create_booking'),
    path('bookings/edit/<str:pk>/', views.edit_booking, name='edit_booking'),
    path('bookings/delete/<str:pk>/', views.delete_booking, name='delete_booking'),

    # rooms
    path('rooms/', views.rooms_list, name="room_list"),
    path('rooms/create/', views.create_room, name='create_room'),
    path('rooms/edit/<str:pk>/', views.edit_room, name='edit_room'),
    path('rooms/delete/<str:pk>/', views.delete_room, name='delete_room'),

    # users
    path('customers/', views.customers_list, name="customer_list"),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/edit/<str:pk>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<str:pk>/', views.delete_customer, name='delete_customer'),

    # authentication api
    path('api/register/', UsersRegistrationAPI.as_view(), name="customer_registration_api"),
    path('api/signin/', UsersSigninAPI.as_view(), name="customer_signin_api"),

    # account api
    path('api/manage_account/', ManageHotelAccountView.as_view(), name="manage_account_api"),
    path('api/profile/', UsersProfileAPI.as_view(), name="profile_account_api"),

]
