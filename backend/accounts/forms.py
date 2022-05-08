from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# first name
# last name
# check if user is already existed

# number of bookings -- customer loyality
# Rewards Points -- for booking purpose
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
