from django.db import models
from django.db.models import Model

# This class represents a currency's spot price at a given timestamp
class SpotPrice(Model):
    base = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    amount = models.FloatField()
    def __str__(self):
        return ("%s-%s: %f" % (self.base, self.currency, self.amount))

# This class represents a list of spot prices for a given currency pair at a given time
class SpotPriceRequest(Model):
    base = models.CharField(max_length=200)
    spot_prices = []
    timestamp = models.DateField()
    def __str__(self):
        return ("%s Spot Prices Count: %s - %s" % (self.base, len(self.spot_prices), self.timestamp))
