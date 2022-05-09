from rest_framework import serializers
from .models import UserProfile


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'user',
            'total_bookings',
            'total_rewards'
        )
