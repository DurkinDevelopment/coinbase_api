from django.urls import path
from .views import Currency

urlpatterns = [
        path('<str:currency_pair>', Currency.get_currency_spot_price, name="get_currency_spot_price"),
]
