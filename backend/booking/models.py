from django.db import models
from accounts.models import Customer, RoomManager
from datetime import date
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Room(models.Model):
    manager = models.ForeignKey(RoomManager, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=5)
    room_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    price = models.FloatField(default=300.00)
    no_of_days_advance = models.IntegerField()
    start_date = models.DateField(auto_now=False,
                                  auto_now_add=False)
    room_image = models.CharField(max_length=500)

    def __str__(self):
        return "Room No: " + str(self.room_no)


class Booking(models.Model):
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.FloatField()
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Booking ID: " + str(self.id)

    @property
    def is_past_due(self):
        return date.today() > self.end_day
