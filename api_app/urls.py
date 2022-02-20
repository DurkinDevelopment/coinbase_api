from django.urls import path
from .views import Currency, Service

urlpatterns = [
        path('health', Service.get_health, name="get_health"),
        path('<str:currency_pair>', Currency.get_currency_spot_price, name="get_currency_spot_price"),
]
