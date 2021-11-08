from alpaca_trade_api.rest import TimeFrame
import schedule
import time

from modules.stockqueries import StockQuery
from modules.stockorders import StockOrder

### Config ###
SEC_KEY = '' # Secret Key Here
PUB_KEY = '' # Public Key Here
LIVE_TRADING = False # For live trading, set to True. For paper trading, set to False.

sq = StockQuery(SEC_KEY, PUB_KEY, LIVE_TRADING)


### Jobs to schedule ###

def job1():
    """Job 1: Every trading day at 14:30 CST, query market to find 5 best fit stocks"""

    print("I'm working on job 1...")
    aaplBars = sq.getStockData('AAPL',TimeFrame.Hour,"2021-11-04","2021-11-04",5)
    print(aaplBars)

schedule.every().day.at("09:35").do(job1)


def job2():
    """Job 2: Every trading day at 14:45 CST, market buy 20% of buying power to each best fit stock"""

    print("I'm working on job 2...")

schedule.every().day.at("09:36").do(job2)


def job3():
    """Job 3: Every trading day at 08:30 CST, monitor best fit stocks for optimal sell point"""

    print("I'm working on job 3...")

schedule.every().day.at("09:37").do(job3)


### Run jobs until program is stopped ###

while True:
    schedule.run_pending()
    time.sleep(60)
