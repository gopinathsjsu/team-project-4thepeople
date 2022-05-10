from django import forms
from django.forms import ModelForm
from .models import Booking, Room

Amenities_Choices = (
    ("Daily Continental Breakfast", "Daily Continental Breakfast"),
    ("Access to fitness room", "Access to fitness room"),
    ("Access to Swimming Pool and Jacuzzi", "Access to Swimming Pool and Jacuzzi"),
    ("Daily Parking", "Daily Parking"),
    ("All meals included", "All meals included")
)


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['room_no', 'user_id', 'number_of_guests', 'booking_location',
                  'booking_room_type', 'booking_amenities', 'start_day', 'end_day', 'amount']

        widgets = {
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'}),
            'booking_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'booking_room_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room type'}),
            'booking_amenities': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amenities'}),
            'start_day': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Starting Date'}),
            'end_day': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ending Date'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_no', 'room_type', 'room_amenities',
                  'price', 'room_location', 'room_image']

        widgets = {
            'room_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'}),
            'room_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'room_amenities': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room type'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'room_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'room_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
        }
