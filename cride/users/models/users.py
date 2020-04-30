"""Users Model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """
    User models.

    Extend from Django's Abtsaract User and local Utilities
    """

    email = models.EmailField(
        "Email addres",
        max_length=254,
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format : +99999999 up to 15 digits allowed'
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=50,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Helps easily distinguish users and perform queries.'
            'Clients are the main type of users.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the users have verified its email address'
    )

    def __str__(self):
        """Retun str username."""
        return self.username

    def get_short_name(self):
        """Return username like the shortname."""
        return self.username
