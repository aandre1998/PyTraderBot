from alpaca_trade_api.rest import TimeFrame
import schedule
import time

from modules.stockqueries import StockQuery
from modules.stockorders import StockOrder

### Config ###
SEC_KEY = '' # Secret Key Here
PUB_KEY = '' # Public Key Here
LIVE_TRADING = False # For live trading, set to True. For paper trading, set to False.
stock_list = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'AMZN'] # This will contain all tickers of interest


queries = StockQuery()
orders = StockOrder(SEC_KEY, PUB_KEY, LIVE_TRADING)


cash_available = int(orders.getAccountInfo()['cash']) # cash available to spend in the account
today = time.strftime("%Y-%m-%d") # Today's date in relevant format
best_fit_stocks = []
stock_price_dict = {}

### Jobs to schedule ###
def data_collection_job():
    """Every trading day at 08:30 CST, start collecting price data for list of stocks.
    This process will end when the schedule is cleared in data_analysis_job at 14:30."""
    
    print("Starting data_collection_job")

    stock_price_dict = queries.createStockPriceDict(stock_list) #initialize dict with empty lists

    def job1():
        for stock in stock_list:
            stock_price_dict[stock].append(queries.getCurrentStockPrice(stock)) #every 15 mins, append lists with current price
        print(stock_price_dict)
    
    job1()
    schedule.every(15).minutes.do(job1)

schedule.every().day.at("08:30").do(data_collection_job)


def data_analysis_job():
    """Every trading day at 14:30, stop the data_collection_job and analyze the data.
    Map each data set to a mathematical model and select the 5 stocks with the best scores."""

    schedule.clear() # clear the schedule so the live data collection stops

    # Map each set of data to a mathematical model, create a dict of scores for each stock
    # model = 5*(#green candles/#total candles) + 2*(daily vol/avg vol) and must be <2% increase on day
    # if #green > 25 & daily/avg > 1.2 & increase <2%:
        #model it out, pick best ones
    # Append best 5 tickers to an empty list - best_fit_stocks

schedule.every().day.at("14:30").do(data_analysis_job)


def buy_stocks_job():
    """Every trading day at 14:45 CST, market buy each best fit stock equally"""

    print("Starting buy_stocks_job")
    
    if len(best_fit_stocks) > 0:
        for stock in best_fit_stocks:
            orders.buyStock(stock, cash_available/len(best_fit_stocks))
    else:
        print("No stocks met the criteria.")

schedule.every().day.at("10:03").do(buy_stocks_job)


def job3():
    """Job 3: Every trading day at 08:30 CST, monitor best fit stocks for optimal sell point"""

    print("I'm working on job 3...")

schedule.every().day.at("17:28").do(job3)


### Run jobs until program is stopped ###

while True:
    schedule.run_pending()
    today = time.strftime("%Y-%m-%d")
    time.sleep(1)