from django.conf import settings
from django.db import models
from datetime import datetime

class StripeToken(models.Model):

    stripe_id = models.CharField(
        max_length=255
    )

    livemode = models.BooleanField(
        default=False
    )

    created = models.IntegerField(
        default=None,
        blank=True,
    )

    used = models.BooleanField(
        default=False,
    )

class Recepient(models.Model):

    created_at = models.DateTimeField(
        default=datetime.now,
        editable=True,
    )

    email = models.EmailField()

    stripe_token = models.ForeignKey('StripeToken')

class Sender(models.Model):

    created_at = models.DateTimeField(
        default=datetime.now,
        editable=True,
    )

    email = models.EmailField()

    bank_routing_number = models.IntegerField(
        default=None
    )

    bank_account_number = models.IntegerField(
        default=None
    )

class Request(models.Model):

    created_at = models.DateTimeField(
        default=datetime.now,
        editable=True,
    )

    recepient = models.ForeignKey('Recepient')

    sender = models.ForeignKey('Sender')

    quantity = models.DecimalField(
        max_digits=65, 
        decimal_places=2,
        default=0.00
    )

    paid = models.BooleanField(
        default=None
    )