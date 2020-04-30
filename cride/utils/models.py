"""Django models utilities."""

# Django
from django.db import models


class CRideModel(models.Model):
    """Comparte Ride base model."""

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which object was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which object was last modified.'
    )

    class Meta:
        """Overwrite super metod."""

        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
