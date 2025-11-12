import os
from alpaca.trading.client import TradingClient

def startScreen():
    s = int(input("What do you want to do \n1. Check connection to Alpaca \n2. Check if something is tradeable\nEnter Here: "))
    if s == 1:
        login()
    else:
        print("Hello")

def login():   
    api_key = os.getenv("APCA_API_KEY_ID")
    secret_key = os.getenv("APCA_API_SECRET_KEY")
    trading_client = TradingClient(api_key, secret_key, paper=True)
    account = trading_client.get_account()
    print(f"Connected to Alpaca!")

startScreen()

