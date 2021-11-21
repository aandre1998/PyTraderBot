import alpaca_trade_api as tradeapi
import ast


class StockOrder:
    """Provides functions that place orders on the stock market using a SEC_KEY and PUB_KEY."""
    

    def __init__(self, SEC_KEY, PUB_KEY, LIVE_TRADING=False):
        if LIVE_TRADING:
            self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY)
        else:
            self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url='https://paper-api.alpaca.markets')
    

    def getAccountInfo(self):
        """Get Alpaca account info such as cash available, buying power, etc."""

        account_info = self.api.get_account()
        account_info = str(account_info)
        account_info = account_info[8:len(account_info)-1]
        account_info = ast.literal_eval(account_info)
        
        return account_info


    def buyStock(self, symbol, quantity):
        """Send a buy order to the stock market through the Alpaca API."""
        print("Buying $" + str(quantity) + " worth of " + symbol)


    def sellStock(self, symbol, quantity):
        """Send a sell order to the stock market through the Alpaca API."""
        print("Selling $" + str(quantity) + " worth of " + symbol)