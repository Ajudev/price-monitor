from channels.layers import get_channel_layer
import asyncio
from celery import shared_task
from celery.utils.log import get_task_logger
from api.helpers import fetch_rates
logger = get_task_logger('__name__')
channel_layer = get_channel_layer()

@shared_task()
def push_live_rates():
    """
    Function which gets triggered by celery worker which works get activated when celery beat schedules the task to be run
    in every 1 minute. The function will fetch latest live rates and push it to web page for viewers to view.
    """
    rates = fetch_rates()
    live_data_txt = f'Exchange Rate: {rates.get("exchange_rate")}, Bid Price: {rates.get("bid_price")}, Ask Price: {rates.get("ask_price")}, Time: {rates.get("fetch_time")}'
    loop = asyncio.get_event_loop()
    coroutine = channel_layer.group_send(
        'broadcast',
        {
            'type': 'send_message',
            'data': live_data_txt
        }
    )
    loop.run_until_complete(coroutine)