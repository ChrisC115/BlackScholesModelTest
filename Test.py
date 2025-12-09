import pandas
import numpy
import matplotlib
import yfinance as yf

apple = yf.Ticker("APPL")


apple = apple.history(period = "1y")
print(apple)
