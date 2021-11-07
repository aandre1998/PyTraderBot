import alpaca_trade_api as tradeapi
from datetime import datetime


class StockOrder:
    """Provides functions that place orders on the stock market using a SEC_KEY and PUB_KEY."""
    

    def __init__(self, SEC_KEY, PUB_KEY, LIVE_TRADING=False):
        if LIVE_TRADING:
            self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY)
        else:
            self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url='https://paper-api.alpaca.markets')
    

    def buyStock(self, symbol, quantity):
        """Send a buy order to the stock market through the Alpaca API."""
        print("Buying " + quantity + " shares of " + symbol)


    def sellStock(self, symbol, quantity):
        """Send a sell order to the stock market through the Alpaca API."""
        print("Selling " + quantity + " shares of " + symbol)