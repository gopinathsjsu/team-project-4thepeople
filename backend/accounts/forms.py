from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['total_bookings', 'total_rewards', 'user_level']

        widgets = {
            'total_bookings': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Bookings'}),
            'total_rewards': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Reward Points'}),
            'user_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Level'}),
        }
