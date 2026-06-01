import pandas as pd
import yfinance as yf

def load_data(ticker, start_date):
    data = yf.download(ticker, start=start_date)
    data = data.dropna()
    return data




