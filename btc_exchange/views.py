from datetime import datetime

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from btc_exchange.btc_engine.common import get_register_crpto_engine
from btc_exchange.constants import DATE_FORMAT


class GetBitcoinPriceView(APIView):
    def get(self, request, *args, **kwargs):
        current_price = get_register_crpto_engine().get_current_price()
        return Response({'price': current_price})


class ListBitcoinPriceView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bitcoin_prices.html'

    def get(self, request, *args, **kwargs):
        """
        Api provide history of bitcoin price between provided start_date and end_date
        If only end date is provided it will provide history for 10 days till the provided
        end date and,
        if only start date is provided it provide history between start date till today.
        If both start date and end date is provided it will provide the price of bitcoin between
        these dates
        """
        default_end_date = datetime.now().date().strftime(DATE_FORMAT)
        start_date = request.GET.get('start_date')
        start_date = start_date and datetime.strptime(start_date, DATE_FORMAT).date() or None
        end_date = datetime.strptime(
            request.GET.get('end_date', default_end_date), DATE_FORMAT
        ).date()
        historical_price = get_register_crpto_engine().get_historical_price(end_date, start_date)
        return Response({'data': historical_price})
