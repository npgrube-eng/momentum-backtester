import pandas as pd
import matplotlib.pyplot as plt
import data_loader as dl


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
