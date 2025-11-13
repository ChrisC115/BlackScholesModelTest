import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = None

def startScreen():
    s = int(input("What do you want to do \n1. Check if something is tradeable\nEnter Here: "))
    if s ==1:
        login()
        tradeSearch()
    else:
        print("hello")

def login():
    global trading_client   
    api_key = os.getenv("APCA_API_KEY_ID")
    secret_key = os.getenv("APCA_API_SECRET_KEY")
    trading_client = TradingClient(api_key, secret_key, paper=True)
    account = trading_client.get_account()
    print(f"Connected to Alpaca!")

def tradeSearch():
    global trading_client
    assetSearch = input("What asset do you want to search for (Use their Shortened Symbol) : ").upper()
    aSearch = trading_client.get_asset(assetSearch)
    if aSearch.tradable:
        print("We can trade",assetSearch)
        startScreen()
    else:
        print("We can't trade",assetSearch)
        startScreen()



startScreen()
