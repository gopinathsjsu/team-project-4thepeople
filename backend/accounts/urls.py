from django.urls import path
from . import views
from .views import UsersRegistrationAPI, UsersSigninAPI, ManageHotelAccountView

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),

    # authentication api
    path('api/register/', UsersRegistrationAPI.as_view(), name="customer_registration_api"),
    path('api/signin/', UsersSigninAPI.as_view(), name="customer_signin_api"),
    path('api/manage_account/', ManageHotelAccountView.as_view(), name="manage_account_api"),

]
