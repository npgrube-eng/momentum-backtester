import pandas as pd
import yfinance as yf

def load_data(ticker, start_date, end_date):
    """
    Downloads historical stock price data.

    Parameters:
        ticker (str): Stock ticker symbol
        start_date (str): YYYY-MM-DD
        end_date (str): YYYY-MM-DD

    Returns:
        pandas.DataFrame
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data.dropna()
    data = data[["Close"]]
    return data




