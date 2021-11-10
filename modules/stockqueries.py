import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import ast
import time
import json
from websocket import create_connection


class StockQuery:
    """Provides functions that query the stock market using the Alpaca API.
    Secret key and public key required."""
    

    def __init__(self, SEC_KEY, PUB_KEY, LIVE_TRADING):
        self.SEC_KEY = SEC_KEY
        self.PUB_KEY = PUB_KEY

        if LIVE_TRADING:
            self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY)
        else:
            self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url='https://paper-api.alpaca.markets')
        
        
    
    
    def getAccountInfo(self):
        """Get account info such as cash available, buying power, etc."""

        account_info = self.api.get_account()
        account_info = str(account_info)
        account_info = account_info[8:len(account_info)-1]
        account_info = ast.literal_eval(account_info)
        
        return account_info



    def getStockData(self, symbol, timeunit, fromdate, todate, amount):
        """Returns a list of dictionaries containing requested market data (time, open, close, volume).
        Each dictionary represents one bar of data."""
        
        stockData = []

        raw_market_data = self.api.get_bars_iter(symbol, timeunit, fromdate, todate, limit=amount, adjustment='raw')
        for bar in raw_market_data:
            bar = str(bar) #convert bar to str
            bar = bar[4:len(bar)-1] #slice to dict format
            bar = ast.literal_eval(bar) #create dict from bar
            bar_formatted = {'time':bar['t'], 'open':bar['o'], 'close':bar['c'], 'volume':bar['v']}
            stockData.append(bar_formatted)

        return stockData

    
    def getRealTime(self):
        iex = create_connection("wss://stream.data.alpaca.markets/v2/iex")
        print(iex.recv())

        iex_auth = {"action": "auth", "key": self.PUB_KEY, "secret": self.SEC_KEY}
        iex_auth = str(iex_auth).replace("'","\042") #convert dict to string and replace ' with "
        iex.send(iex_auth)
        print(iex.recv())

        subscribe = {"action":"subscribe","bars":["AAPL","MSFT","TSLA"]}
        subscribe = str(subscribe).replace("'","\042")
        iex.send(subscribe)
        print(iex.recv())
        #iex.send({"action":"subscribe","trades":["AAPL"],"quotes":["AMD","CLDR"],"bars":["AAPL","VOO"]})

        while True:
            result = iex.recv()
            result = json.loads(result)
            print ("Received '%s'" % result)
            time.sleep(1)

        iex.close()