from coinbase.wallet.client import Client

# TODO: Abstract these out using .env file & secrets manager
API_KEY = 'BfgzvUAomY2ZxW4t'
API_SECRET = 'GmqcDXjUvZqczyOOuBbeq5eOdYxrG3mi' 

# Initiate the coinbase client
client = Client(API_KEY, API_SECRET)

class CoinbaseAPI:
    def get_spot_price(tag):
        price = client.get_spot_price(currency_pair = tag)
