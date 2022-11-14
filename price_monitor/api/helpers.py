from requests import get
from django.conf import settings
from typing import Dict


def fetch_rates() -> Dict[str, float]:
    """
    Function which will fetch the rates from api, format the data to the required format and 
    sends the data back.
    """
    api_details = getattr(settings, 'PRICE_API_DETAILS')
    url = api_details.get('url')
    params = api_details.get('params')

    request = get(url, params=params)
    price_data = request.json().get('Realtime Currency Exchange Rate', {})
    mod_data = {}

    for key,value in price_data.items():
        if key == '1. From_Currency Code':
            mod_data['from_curr_code'] = value
        elif key == '3. To_Currency Code':
            mod_data['to_curr_code'] = value
        elif key == '5. Exchange Rate':
            mod_data['exchange_rate'] = float(value)
        elif key == '6. Last Refreshed':
            mod_data['fetch_time'] = value
        elif key == '8. Bid Price':
            mod_data['bid_price'] = float(value)
        elif key == '9. Ask Price':
            mod_data['ask_price'] = float(value)

    return mod_data