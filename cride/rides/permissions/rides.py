"""Rides permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsRideOwner(BasePermission):
    """Rides permissions."""

    def has_object_permission(self, request, view, obj):
        """Allow access only to rides owner."""
        return request.user == obj.offered_by
