from rest_framework import serializers
from booking.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '_all_'
