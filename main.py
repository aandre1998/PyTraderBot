from alpaca_trade_api.rest import TimeFrame
import schedule
import time

from modules.stockqueries import StockQuery
from modules.stockorders import StockOrder

### Config ###
SEC_KEY = '' # Secret Key Here
PUB_KEY = '' # Public Key Here
LIVE_TRADING = False # For live trading, set to True. For paper trading, set to False.

queries = StockQuery(SEC_KEY, PUB_KEY, LIVE_TRADING)
orders = StockOrder(SEC_KEY, PUB_KEY, LIVE_TRADING)

best_fit_stocks = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'AMZN'] # This will be an empty list ready for the top 5
cash_available = int(queries.getAccountInfo()['cash'])
today = time.strftime("%Y-%m-%d")

### Jobs to schedule ###

def job1():
    """Job 1: Every trading day at 14:30 CST, query market to find 5 best fit stocks"""

    print("I'm working on job 1...")
    
    for stock in best_fit_stocks: # Get time, open, close, volume for 5 hours of 11-04 for each stock
        print(stock + " Data")
        stockBars = queries.getStockData(stock,TimeFrame.Hour,"2021-11-04","2021-11-04",5)
        for bar in stockBars:
            print(bar)

schedule.every().day.at("13:51").do(job1)


def job2():
    """Job 2: Every trading day at 14:45 CST, market buy 20% of cash available to each best fit stock"""

    print("I'm working on job 2...")
    
    for stock in best_fit_stocks: # Buy each stock with 20% of cash available
        orders.buyStock(stock, cash_available/5)


schedule.every().day.at("13:52").do(job2)


def job3():
    """Job 3: Every trading day at 08:30 CST, monitor best fit stocks for optimal sell point"""

    print("I'm working on job 3...")

schedule.every().day.at("13:53").do(job3)


### Run jobs until program is stopped ###

#print(queries.getStockData('AAPL',TimeFrame.Hour,today,today,5)) this does not work because
#API does not allow data from past 15 mins.

while True:
    schedule.run_pending()
    today = time.strftime("%Y-%m-%d")
    time.sleep(60)
