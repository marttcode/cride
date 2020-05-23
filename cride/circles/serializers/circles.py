"""Circle Serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from cride.circles.models import Circle


class CircleModelSerializer(serializers.ModelSerializer):
    """Circle Model Serializer."""

    class Meta:
        """Meta class."""
        model = Circle
        fields = (
            'id', 'name', 'slug_name',
            'about', 'picture',
            'rides_offered', 'rides_taken',
            'is_limited', 'members_limit'
        )
