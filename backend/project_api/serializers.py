from rest_framework import serializers
from booking.models import Room, Contact


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '_all_'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '_all_'
