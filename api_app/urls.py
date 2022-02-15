from django.urls import path
from .views import Currency

urlpatterns = [
    path('', Currency.as_view()),
]
