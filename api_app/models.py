from django.db import models
from django.db.models import Model

# This class represents a currency's spot price at a given timestamp
class SpotPrice(Model):
    currency = models.CharField(max_length=200)
    base = models.CharField(max_length=200)
    amount = models.FloatField()

# This class represents a list of spot prices for a given currency pair at a given time
class SpotPriceRequest(Model):
    base = models.CharField(max_length=200)
    spot_prices = []
    timestamp = models.DateField()
