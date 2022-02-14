from django.urls import path
from .views import GetCurrency

urlpatterns = [
    path('', GetCurrency.as_view()),
]
