"""Membership Serializer."""

# Django REST Framework
from rest_framework import serializers

# Serializer
from cride.users.serializers import UserModelSerializer

# Models
from cride.circles.models import Membership, Invitation

# Utilities
from django.utils import timezone


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


class AddMemberSerializer(serializers.Serializer):
    """Add member serializer.

    Handle the addition of a new member to circle.
    Circle object must be provided in the context.
    """
    invitation_code = serializers.CharField(min_length=8)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_user(self, data):
        """Verify user isn't already a member."""
        circle = self.context['circle']
        user = data
        query = Membership.objects.filter(circle=circle, user=user)

        if query.exists():
            raise serializers.ValidationError('User is already member of this circle')
        return data

    def validate_invitation_code(self, data):
        """Verify code exists and that it is related to the circle."""
        try:
            invitation = Invitation.objects.get(
                code=data,
                circle=self.context['circle'],
                used=False,
            )
        except Invitation.DoesNotExist:
            raise serializers.ValidationError('Invalid invitation code.')
        self.context['invitation'] = invitation
        return data

    def validate(self, data):
        """Verify circle is capable of accepting a new members."""
        circle = self.context['circle']
        if circle.is_limited and circle.members.count() >= circle.members_limit:
            raise serializers.ValidationError('Circle has reached its members limit.')
        return data

    def create(self, validated_data):
        """Create new circle member."""
        circle = self.context['circle']
        invitation = self.context['invitation']
        user = validated_data['user']
        date = timezone.now()

        # Member creation
        member = Membership.objects.create(
            user=user,
            profile=user.profile,
            circle=circle,
            invited_by=invitation.issued_by,
        )

        # Update Invitation
        invitation.used_by = user
        invitation.used = True
        invitation.used_at = date
        invitation.save()

        # Update Invitation user
        issuer = Membership.objects.get(user=invitation.issued_by, circle=circle)
        issuer.user_invitation += 1
        issuer.remaining_invitation -= 1
        issuer.save()

        return member
