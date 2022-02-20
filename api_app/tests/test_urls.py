from django.urls import reverse, resolve
from django.urls import path

class TestUrls: 
    # Validate that each of the path's view names are correct for each url
    def test_get_metrics_url(self):  
        path = reverse('get_metrics')
        assert resolve(path).view_name == "get_metrics"
        
    def test_get_health_url(self):  
        path = reverse('get_health')
        assert resolve(path).view_name == "get_health"
        
    def test_get_currency_spot_price_url(self):  
        path = reverse('get_currency_spot_price', kwargs={'currency_pair':'USD'})
        assert resolve(path).view_name == "get_currency_spot_price"

