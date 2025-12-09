#pip install pandas numpy yfinance matplotlib

import pandas as pd
import numpy
import matplotlib.pyplot as plt
import yfinance as yf


ticker_strings = ['AAPL', 'MSFT', 'GOOG']
df_list = []

for ticker_symbol in ticker_strings:
    # Download data
    stock_data = yf.download(ticker_symbol, period='1mo')
    # Add a 'ticker' column for identification
    stock_data['Ticker'] = ticker_symbol
    # Append the DataFrame to the list
    df_list.append(stock_data)

# 'df_list' is now a list containing three separate pandas DataFrames
print("\nNumber of DataFrames in the list:", len(df_list))
print("Head of the first DataFrame (AAPL):")
print(df_list[0].head())

