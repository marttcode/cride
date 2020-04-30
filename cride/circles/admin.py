"""Circles admin."""

# Django
from django.contrib import admin

# Model
from cride.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle admin."""

    list_display = (
        'slug_name',
        'is_public',
        'members_limit'
    )

    search_fields = ('slug_name', 'name')
    list_filter = (
        'is_public',
        'verified'
    )
