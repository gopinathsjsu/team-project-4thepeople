from django.contrib import admin
from .models import Contact, Room, Booking

# Register your models here.
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Booking)
