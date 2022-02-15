from django.db import models

# This class represents a currency's spot price at a given timestamp
class SpotPrice(models.Model):
    currency = models.CharField(max_length=200)
    amount = models.FloadField()
    timestamp = models.DateField()
