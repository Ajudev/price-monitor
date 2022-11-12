from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

PRICE_API_DETAILS = {
    'url': 'https://www.alphavantage.co/query',
    'params': {
        'function': 'CURRENCY_EXCHANGE_RATE',
        'from_currency': 'BTC',
        'to_currency': 'USD',
        'apikey': os.getenv('API_KEY')
    }
}