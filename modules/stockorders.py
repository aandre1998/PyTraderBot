import alpaca_trade_api as tradeapi
from datetime import datetime

class StockOrder:
    """Provides functions that place orders on the stock market using a SEC_KEY and PUB_KEY."""
    
    def __init__(self, SEC_KEY, PUB_KEY, BASE_URL):
        self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)