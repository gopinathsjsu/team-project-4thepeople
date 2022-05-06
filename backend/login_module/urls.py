from django.urls import path, include
from . views import user_signup, user_sigin, manager_signin

urlpatterns = [
    path('signup/', user_signup, name='user_signup'),
    path('signin/', user_sigin, name='user_signin'),
    path('manager_signin/', manager_signin, name='manager_signin'),
]
