from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_bookings = models.IntegerField(default=0)
    total_rewards = models.IntegerField(default=0)
    user_level = models.CharField(default="silver", max_length=50)

    def __str__(self):
        return "Customer: " + self.user.first_name + " " + self.user.last_name


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
