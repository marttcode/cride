"""Invitations permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsSelfMember(BasePermission):
    """Allow access only to members owner."""

    def has_permission(self, request, view):
        """Let object permission grant access."""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Allow access only if member is owned by the requesting user."""
        return request.user == obj.user
