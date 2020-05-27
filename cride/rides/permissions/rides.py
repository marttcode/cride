"""Rides permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsRideOwner(BasePermission):
    """Rides permissions."""

    def has_object_permission(self, request, view, obj):
        """Allow access only to rides owner."""
        return request.user == obj.offered_by


class IsNotRideOwner(BasePermission):
    """Verify if user is not ride Owner."""

    def has_object_permission(self, request, view, obj):
        return not request.user == obj.offered_by
