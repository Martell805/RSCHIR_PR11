import datetime

from django.db import models

# Create your models here.
from django.conf import settings


class Analytics(models.Model):
    date = models.DateField(default=datetime.datetime.now())
    image = models.BinaryField()

    class Meta:
        app_label = 'RSCHIR_PR11'
