from django.conf import settings
from django.db import models
from datetime import datetime

class Recepient(models.Model):

    created_at = models.DateTimeField(
        default=datetime.now,
        editable=True,
    )

    email = models.EmailField()

    stripe_toke = models.CharField(
    	max_length=255
    )

class Sender(models.Model):

    created_at = models.DateTimeField(
        default=datetime.now,
        editable=True,
    )

    email = models.EmailField()

    stripe_toke = models.CharField(
    	max_length=255
    )

class Request(models.Model):

    created_at = models.DateTimeField(
        default=datetime.now,
        editable=True,
    )

    recepient = models.ForeignKey('Recepient')

    sender = models.ForeignKey('Sender')

    stripe_toke = models.CharField(
    	max_length=255
    )