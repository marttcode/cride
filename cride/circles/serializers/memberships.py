"""Membership Serializer."""

# Django REST Framework
from rest_framework import serializers

# Serializer
from cride.users.serializers import UserModelSerializer

# Models
from cride.circles.models import Membership


class MembershipModelSerializer(serializers.ModelSerializer):
    """Membership Model Serializer."""

    user = UserModelSerializer(read_only=True)
    invited_by = serializers.StringRelatedField()
    joined_at = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """Meta class."""

        model = Membership
        fields = (
            'user',
            'is_admin', 'is_active',
            'user_invitation', 'remaining_invitation',
            'invited_by', 'rides_offered',
            'joined_at',
        )
        read_only_fields = (
            'user',
            'user_invitation',
            'invited_by',
            'joined_at',
            'rides_offered', 'rides_token',
        )
