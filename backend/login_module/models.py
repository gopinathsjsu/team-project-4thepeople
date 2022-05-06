from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    pin_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Customer: " + self.username


class RoomManager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return "Room Manager: " + self.username
