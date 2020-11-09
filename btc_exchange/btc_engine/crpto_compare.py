import logging
from datetime import date

import requests
from django.conf import settings

from btc_exchange.btc_engine.common import BaseCrptoEngine
from btc_exchange.constants import DATE_FORMAT

logger = logging.getLogger(__name__)


class CrptoCompareEngine(BaseCrptoEngine):
    CONVERSION_SYMBOL = 'fsym=BTC&tsym=USD'

    def __init__(self):
        crpto_compare_config = settings.SERVER_CONFIG.get('crpto_compare')
        if not crpto_compare_config:
            raise Exception('crpto_compare Config is required in settings.SERVER_CONFIG')
        self.api_key = crpto_compare_config.get('api_key')
        self.base_url = crpto_compare_config.get('base_url')

    def get_historical_price(self, end_date: date, start_date: date = None, ):
        if start_date:
            delta = end_date - start_date
            limit = delta.days
        else:
            limit = 9
        to_timestamp = int(end_date.strftime('%s'))
        url = (
            f'{self.base_url}data/v2/histoday?api_key={self.api_key}&fsym=BTC&tsym=USD'
            f'&limit={limit}&toTs={to_timestamp}'
        )
        logger.info('Getting crpto history data using url %s', url)
        historical_price = requests.get(url).json().get('Data', {}).get('Data')
        return history_data_parser(historical_price)

    def get_current_price(self):
        url = f'{self.base_url}data/price?api_key={self.api_key}&fsym=BTC&tsyms=USD'
        return requests.get(url).json().get('USD')


def history_data_parser(data):
    return list(reversed([{
        'price': d.get('close'),
        'for_date': date.fromtimestamp(d.get('time')).strftime(DATE_FORMAT)
    } for d in data]))
