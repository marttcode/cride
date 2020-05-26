"""Rides serializer."""

# Django REST framework
from rest_framework import serializers

# Models
from cride.rides.models import Ride

# Utilities
from datetime import timedelta
from django.utils import timezone


class CreateRideSerializer(serializers.ModelSerializer):
    """Rides serializer."""

    offered_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    available_seats = serializers.IntegerField(min_value=1)

    class Meta:
        """Meta class."""

        model = Ride
        exclude = ('offered_in', 'passengers', 'rating', 'is_active')

    def validate_departure_date(self, data):
        """Verify date is not in the past."""
        min_date = timezone.now() + timedelta(minutes=15)
        if data < min_date:
            raise serializers.ValidationError(
                'Departure time must be at lasted passing the next 20 minutes window.'
            )
        return data
