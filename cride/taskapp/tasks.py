"""Celery Tasks."""

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from cride.users.models import User
from cride.rides.models import Ride

# Utilities
from datetime import timedelta
import time
import jwt

# Celery
from celery.decorators import task, periodic_task


@task(name='send_confirmation_email', max_retires=3)
def send_confirmation_email(user__pk):
    """Send account verification link to given user."""
    for i in range(30):
        time.sleep(1)
        print("Sleeping " + str(i + 1))
    user = User.objects.get(pk=user__pk)
    verification_token = gen_verification_token(user)
    subject = "Welcome @{}!, Verify your account to start using comparte Ride".format(user.username)
    from_email = 'Comparte Ride <noreply@comparteride.com>'
    to = user.email
    content = render_to_string(
        'email/users/account_verification.html',
        {'token': verification_token, 'user': user}
    )

    msg = EmailMultiAlternatives(subject, content, from_email, [to])
    msg.attach_alternative(content, "text/html")
    msg.send()


def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation',
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return token.decode()


#@periodic_task(name='disable_finish_rides', run_every=timedelta(minutes=15))
def disable_finish_rides():
    """Disable finish rides."""
    now = timezone.now()
    offset = now + timedelta(seconds=15)

    # Update rides that have already finished
    rides = Ride.objects.filter(
        arrival_date__gte=now,
        arrival_date__lte=offset,
        is_active=True
    )
    rides.update(is_active=False)
