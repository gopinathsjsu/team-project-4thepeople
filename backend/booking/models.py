from django.db import models
from datetime import date
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

Amenities_Choices = (
    ("Daily Continental Breakfast", "Daily Continental Breakfast"),
    ("Access to fitness room", "Access to fitness room"),
    ("Access to Swimming Pool and Jacuzzi", "Access to Swimming Pool and Jacuzzi"),
    ("Daily Parking", "Daily Parking"),
    ("All meals included", "All meals included")
)


class Room(models.Model):
    room_no = models.CharField(max_length=5)
    room_type = models.CharField(max_length=50)
    room_amenities = MultiSelectField(choices=Amenities_Choices, default="Daily Parking")
    is_available = models.BooleanField(default=True)
    price = models.FloatField(default=300.00)
    start_date = models.DateField(auto_now=True, auto_now_add=False)
    room_location = models.CharField(max_length=50, default="San Jose")
    room_image = models.CharField(max_length=500)

    def __str__(self):
        return "Room No: " + str(self.room_no)


class Booking(models.Model):
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_guests = models.IntegerField(default=1)
    booking_location = models.CharField(max_length=50, default="San Jose")
    booking_room_type = models.CharField(max_length=50, default="Studio")
    booking_amenities = MultiSelectField(choices=Amenities_Choices,
                                         default="Daily Parking")
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.FloatField()
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Booking ID: " + str(self.id)

    @property
    def is_past_due(self):
        return date.today() > self.end_day
