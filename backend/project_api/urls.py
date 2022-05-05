from django.urls import path
from .views import UsersSignupAPI,UsersSigninAPI

urlpatterns = [
   path('users/signup/', UsersSignupAPI.as_view(), name="users_signup_api"),
   path('users/signin/', UsersSigninAPI.as_view(), name="users_signin_api"),
]
