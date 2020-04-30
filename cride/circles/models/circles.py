"""Circles models."""

# Django
from django.db import models

# Utilities

from cride.utils.models import CRideModel


class Circle(CRideModel):
    """
    Circle model.

    A circule is a private group where rides are offered and taken
    by its members. To join a circle a user must receive
    an unique invitation code from an existing circle member.
    """

    name = models.CharField("circule name", max_length=150)
    slug_name = models.SlugField(unique=True, max_length=40)
    about = models.CharField('circle description', max_length=255)

    picture = models.ImageField(
        upload_to='circles/pictures',
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True
    )

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(
        'verifief circle',
        default=False,
        help_text='Verified cicles are also know as official communities.'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so everyone knows about their existence.'
    )

    is_limited = models.BooleanField(
        'limited group',
        default=False,
        help_text='Limited cicles can grow up to fixed number of members.'
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If cicles is limited, this will be the limit on the number of menbers.'
    )

    def __str__(self):
        """Return self name."""
        return self.name

    class Meta(CRideModel.Meta):
        """Meta Class."""

        ordering = ['-rides_taken', '-rides_offered']    
