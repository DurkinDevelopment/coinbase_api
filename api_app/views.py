from django.shortcuts import render
from django.http import JsonResponse
import json

# This function is used to retrieve the currency information from the coinbase api based on the tag
class GetCurrency(View):
    def get(self, request):

        # Extract the currency tag from the request body
        data = json.loads(request.body.decode("utf-8"))
        # Validate that the data is a valid currency tag

        # Make an api request to the coinbase api using the validated currency tag

        # Validate that the coinbase request was successful

        # Return the appropriate status code and response payload based on the coinbase api request validation


