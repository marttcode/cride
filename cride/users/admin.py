"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from cride.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'is_staff')
    list_filter = ('created', 'modified')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('reputation', 'rides_taken', 'rides_offered')
    list_filter = ('user__username', 'reputation')


admin.site.register(User, CustomUserAdmin)
