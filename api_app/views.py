from django.views import View
from django.http import JsonResponse
import json
from .models import SpotPrice
from tools.coinbase import CoinbaseAPI
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# This function is used to retrieve the currency information from the coinbase api based on the tag
@method_decorator(csrf_exempt, name='dispatch')
class Currency(View):
    def get(self, request):
        print("inside currency")
        # Extract the currency tag from the request body
        data = json.loads(request.body.decode("utf-8"))

        # Validate that the data is a valid currency tag
        print(data)

        # Make an api request to the coinbase api using the validated currency tag
        get_spot_price_response = CoinbaseAPI.get_spot_price(data) 

        # Validate that the coinbase request was successful
        print("get_spot_price: \n" )
        print(get_spot_price_response)

        # Return the appropriate status code and response payload based on the coinbase api request validation


