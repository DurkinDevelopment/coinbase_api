from django.db import models
from django.db.models import Model

# This class represents a currency's spot price at a given timestamp
class SpotPrice(Model):
    currency = models.CharField(max_length=200)
    amount = models.FloatField()
    timestamp = models.DateField()
