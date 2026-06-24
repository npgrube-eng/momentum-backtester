import pandas as pd
import matplotlib.pyplot as plt
import data_loader as dl
import indicators

ticker = "SPY"

df = dl.load_data(
    ticker,
    start_date="2020-01-01",
    end_date="2021-01-01"
)

print(df.info())
print(df.describe())
plt.plot(df['Close'])
plt.title('Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()




df = indicators.add_sma(df, 20)
df = indicators.add_sma(df, 50)

plt.figure(figsize=(12,6))

plt.plot(df.index, df["Close"], label="Close")
plt.plot(df.index, df["SMA_20"], label="20 Day SMA")
plt.plot(df.index, df["SMA_50"], label="50 Day SMA")

plt.legend()
plt.show()