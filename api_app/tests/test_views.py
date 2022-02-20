import pytest
import json
from django.urls import reverse
from rest_framework.test import APIClient
from api_app.views import Currency, Service


class TestCurrencyView:
    @pytest.mark.django_db
    def test_get_currency_spot_price_usd(self):
        client = APIClient()
        url = reverse('get_currency_spot_price', args=['USD'])
        response = client.get(url, format=json)
        assert response.status_code == 200
        assert len(response.data.data) > 1

    @pytest.mark.django_db
    def test_get_currency_spot_price_eur(api_client):
        client = APIClient()
        url = reverse('get_currency_spot_price', args=['EUR'])
        response = client.get(url, format=json)
        assert response.status_code == 200
        assert len(response.data.data) > 1
        
    @pytest.mark.django_db
    def test_get_currency_spot_price_gbp(api_client):
        client = APIClient()
        url = reverse('get_currency_spot_price', args=['GBP'])
        response = client.get(url, format=json)
        assert response.status_code == 200
        assert len(response.data.data) > 1

    @pytest.mark.django_db
    def test_get_currency_spot_price_jpy(api_client):
        client = APIClient()
        url = reverse('get_currency_spot_price', args=['JPY'])
        response = client.get(url, format=json)
        assert response.status_code == 200
        assert len(response.data.data) > 1

    @pytest.mark.django_db
    def test_get_currency_spot_invalid_pair(client):
        client = APIClient()
        url = reverse('get_currency_spot_price', args=['USDF'])
        response = client.get(url, format=json)
        assert response.status_code == 400
        

class TestServiceView:
    @pytest.mark.django_db
    def test_get_health(self):
        client = APIClient()
        url = reverse('get_health')
        response = client.get(url, format='json')
        assert response.status_code == 200
        assert response.data["isHealthy"] == "true"

    @pytest.mark.django_db
    def test_get_metrics(self):
        client = APIClient()
        url = reverse('get_metrics')
        response = client.get(url, format='json')
        data = response.data
        assert response.status_code == 200
        assert 'cpus' in data
