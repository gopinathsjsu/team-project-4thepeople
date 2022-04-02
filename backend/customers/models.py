from django.db import models


# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email_address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.IntegerField(blank=True)

    """
    profile_image = models.ImageField(upload_to="media", 
                                    height_field=None, 
                                    width_field=None, max_length=None, blank=True)
    """

    def __str__(self):
        return "Customer: " + self.username


class RoomManager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email_address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return "Room Manager: " + self.username
