"""Profile model."""

# Django
from django.db import models

# Utilities

from cride.utils.models import CRideModel


class Profile(CRideModel):
    """
    Profile model.

    A profile holds a user's public data like
    biography, picture and statistcs.
    """

    user = models.OneToOneField(
        "users.User",
        verbose_name='User profile',
        on_delete=models.CASCADE
    )

    picture = models.ImageField(
        "profile picture",
        upload_to='users/pictures',
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank=True)

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation on the rodes taken and offered."
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
