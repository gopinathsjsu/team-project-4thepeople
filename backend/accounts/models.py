from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
