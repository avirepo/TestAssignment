# Create your tests here.
from datetime import datetime, timedelta

from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from btc_exchange.constants import DATE_FORMAT

client = APIClient()


class GetListPriceTestCases(TestCase):
    def test_valid_get_price(self):
        response = client.get(reverse('btc_price'))
        self.assertEqual(response.status_code, 200, 'Api should return success')

    def test_history_price_view(self):
        response = client.get(reverse('btc_history'))
        self.assertEqual(response.status_code, 200, 'Api should return success')

    def test_history_price_view_with_only_start_date(self):
        url = reverse('btc_history')
        days_delta = 7
        start_date = (datetime.now() - timedelta(days=days_delta - 1)).date().strftime(DATE_FORMAT)
        response = client.get(f'{url}?start_date={start_date}')
        self.assertEqual(response.status_code, 200, 'Api should return success')
        self.assertEqual(
            len(response.data.get('data')), days_delta,
            f'Length should be {days_delta} as start and end date is provided'
        )

    def test_history_price_view_with_only_end_date(self):
        url = reverse('btc_history')
        response = client.get(f'{url}?end_date=2020-11-05')
        self.assertEqual(response.status_code, 200, 'Api should return success')
        self.assertEqual(
            len(response.data.get('data')), 10,
            'Length should be 10 as start and end date is provided'
        )

    def test_history_price_view_with_dates(self):
        url = reverse('btc_history')
        response = client.get(f'{url}?start_date=2020-11-01&end_date=2020-11-05')
        self.assertEqual(response.status_code, 200, 'Api should return success')
        self.assertEqual(
            len(response.data.get('data')), 5,
            'Length should be 5 as start and end date is provided'
        )
