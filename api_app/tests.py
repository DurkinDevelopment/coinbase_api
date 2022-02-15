from django.test import TestCase

class ViewsTestCase(TestCase):
        # Test that the expected currency pairs return a 200
        ## Investigate individual tests vs iteratively testing each 
        def test_get_currency_spot_price_usd
            response = self.client.get('/USD')
            self.assertEqual(response.status_code, 200)

