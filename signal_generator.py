
def generate_signals(df):
    """
    Generates trading signals based on SMA crossovers.

    Parameters:
        df (pandas.DataFrame): The input DataFrame with SMA columns

    Returns:
        pandas.DataFrame: DataFrame with signals added
    """
    df["Signal"] = 0  # Default to no signal
    df.loc[df["SMA_20"] > df["SMA_50"], "Signal"] = 1  # Buy signal

    return df
