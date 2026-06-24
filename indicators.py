import pandas as pd

def add_sma(df, window):
    """

    Calculates the Simple Moving Average (SMA) and adds it as a new column to the DataFrame.

    Parameters:
        df (pandas.DataFrame): The input DataFrame
        window (int): The window size for the moving average

    Returns:
        pandas.DataFrame
    """
    df[f"SMA_{window}"] = (df["Close"].rolling(window=window).mean())

    return df