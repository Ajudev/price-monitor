from django.db import models



class Price(models.Model): 
    """
    Model which stores real time currency exchange rate for crypto coins with fiat currencies
    """

    from_curr_code = models.CharField(verbose_name="From Currency Code", max_length=4)
    to_curr_code = models.CharField(verbose_name="To Currency Code", max_length=4)
    fetch_time = models.CharField(verbose_name="API Fetch Time", max_length=20)
    exchange_rate = models.DecimalField(verbose_name="Exchange Rate", max_digits=15, decimal_places=2)
    bid_price = models.DecimalField(verbose_name="Bid Price", max_digits=15, decimal_places=2)
    ask_price = models.DecimalField(verbose_name="Ask Price", max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(verbose_name="Entry Create Datetime", auto_now_add=True)
