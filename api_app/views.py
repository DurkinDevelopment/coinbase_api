from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .models import SpotPrice
from coinbase.wallet.client import Client

# TODO: Abstract these out using .env file & secrets manager
API_KEY = 'BfgzvUAomY2ZxW4t'
API_SECRET = 'GmqcDXjUvZqczyOOuBbeq5eOdYxrG3mi'

# Initiate the coinbase client
client = Client(API_KEY, API_SECRET)

# This function is used to retrieve the currency information from the coinbase api based on the tag
class Currency(APIView):
    # This function is used as a wrapper function for the entry point of the api request
    @api_view(('GET',))
    @csrf_exempt
    def get_currency_spot_price(request, currency_pair):
        # TODO: Create a new get_currency_spot_price_request for auditing
        # Use the coinbase api wrapper function for making a get spot price request
        try:
            get_spot_price_response = CoinbaseAPI.get_spot_price(currency_pair)
            return Response(get_spot_price_response, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

class Service(APIView):
    @api_view(('GET',))
    @csrf_exempt
    def get_health(request):
        data = {
            "isHealthy": "true",
        }
        return Response(data, status=status.HTTP_200_OK) 

# TODO: This can be abstracted out into it's own file
# This class if used for any wrapper functions needed for interacting with the coinbase api
class CoinbaseAPI:
    def get_spot_price(currency_pair_to_query):
        price = client.get_spot_price(currency_pair = currency_pair_to_query)
        return price

