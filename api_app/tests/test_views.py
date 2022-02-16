import pytest
from django.urls import reverse

class Test_Currency_View
    @pytest.mark.django_db
    def test_get_currency_spot_price_usd(cient):
        url = reverse('get_currency_spot_price', kwargs={'currency-pair':'USD'})
        response = cient.get(url)
        assert response.status_code == 200
        assert len(response.data) > 1
    def test_get_currency_spot_price_eur(cient):
        url = reverse('get_currency_spot_price', kwargs={'currency-pair':'EUR'})
        response = cient.get(url)
        assert response.status_code == 200
        assert len(response.data) > 1
    def test_get_currency_spot_price_gbp(cient):
        url = reverse('get_currency_spot_price', kwargs={'currency-pair':'GBP'})
        response = cient.get(url)
        assert response.status_code == 200
        assert len(response.data) > 1
    def test_get_currency_spot_price_jpy(cient):
        url = reverse('get_currency_spot_price', kwargs={'currency-pair':'JPY'})
        response = cient.get(url)
        assert response.status_code == 200
        assert len(response.data) > 1
