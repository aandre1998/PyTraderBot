import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import ast

from modules.stockqueries import StockQuery


SEC_KEY = '' # Secret Key Here
PUB_KEY = '' # Public Key Here
BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading


sq = StockQuery(SEC_KEY, PUB_KEY, BASE_URL)
aaplBars = sq.getStockData('AAPL',TimeFrame.Hour,"2021-11-04","2021-11-04",5)


for bar in aaplBars:
    print(bar)