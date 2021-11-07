import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import ast


class StockQuery:
    """Provides functions that query the stock market using the Alpaca API.
    Secret key and public key required."""
    

    def __init__(self, SEC_KEY, PUB_KEY, LIVE_TRADING=False):
        if LIVE_TRADING:
            self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY)
        else:
            self.api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url='https://paper-api.alpaca.markets')
    
    
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