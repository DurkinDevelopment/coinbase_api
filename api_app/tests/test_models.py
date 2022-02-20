import pytest
from api_app.models import SpotPrice

@pytest.mark.django_db
def test_spot_price_create():
    #Create dummy data
    spot_price = SpotPrice.objects.create(
        base="USD",
        currency="BTC",
        amount=20.22,
    )
    # Assert the dummy data saved as expected
    assert spot_price.base == "USD"
    assert spot_price.currency == "BTC"
    assert spot_price.amount == 20.22
