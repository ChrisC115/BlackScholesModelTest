import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

trading_client = None
data_client = None

def login():
    global trading_client, data_client
    api_key = os.getenv("APCA_API_KEY_ID")
    secret_key = os.getenv("APCA_API_SECRET_KEY")
    
    trading_client = TradingClient(api_key, secret_key, paper=True)
    data_client = StockHistoricalDataClient(api_key, secret_key)
    
    account = trading_client.get_account()
    print(f"Connected to Alpaca! Account status: {account.status}")

def tradeSearch():
    global trading_client
    assetSearch = input("What asset do you want to search for (Use their Shortened Symbol): ").upper()
    aSearch = trading_client.get_asset(assetSearch)
    if aSearch.tradable:
        print("We can trade", assetSearch)
    else:
        print("We can't trade", assetSearch)

def getStockData(symbol):
    global data_client
    request_params = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Day,
        start=datetime(2023, 1, 1),
        end=datetime(2023, 12, 31)
    )
    stock_bars = data_client.get_stock_bars(request_params)
    df = stock_bars.df
    print(df.head())

def startScreen():
    s = int(input("What do you want to do \n1. Check if something is tradeable\n2. Get stock data\nEnter Here: "))
    if s == 1:
        login()
        tradeSearch()
    elif s == 2:
        login()
        symbol = input("Enter symbol: ").upper()
        getStockData(symbol)
    else:
        print("Invalid option.")

startScreen()
