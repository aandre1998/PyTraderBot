import requests
from bs4 import BeautifulSoup


class StockQuery:
    """Provides functions that query the stock market by scraping Yahoo Finance.
    Also provides access to Alpaca account info, secret key and public key required."""


    def getCurrentStockPrice(self, ticker):
        """Scrapes the Yahoo Finance page for given ticker for current price.
        More functionality coming soon."""

        stock_list_prices = {}

        url = "https://finance.yahoo.com/quote/" + ticker
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find('span',attrs={"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}) # This produces unexpected content. ERROR
        fixed_results = results.text.replace(",","")

        try:
            return float(fixed_results) #This can produce an error if the website returns the wrong data, so handle it here
        except:
            return 0.0


    def createStockPriceDict(self, stock_list):
        """Given a list of stocks in format: ["MSFT","AAPL","TSLA"]
        returns a dict of stocks in format: {"MSFT":[],"AAPL":[],"TSLA":[]}
        This is to initialize empty lists for each ticker to receive price data throughout the trading day"""
        
        stock_price_dict = {}

        for stock in stock_list:
            stock_price_dict[stock] = []

        return stock_price_dict
