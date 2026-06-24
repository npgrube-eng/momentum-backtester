# Momentum Backtester

## Moving Averages

A simple moving average (SMA) is a technical indicator that measures the average stock price over a trailing window of time. As each trading day closes, the oldest observation is removed and the newest observation is added, creating a continuously updated average.

Moving averages are often used to identify trends and smooth out short-term price fluctuations. By comparing a short-term moving average to a long-term moving average, traders can gain insight into changes in market momentum.

This project uses a 20-day and 50-day simple moving average. When the 20-day moving average rises above the 50-day moving average, the strategy interprets this as positive momentum. When the 20-day moving average falls below the 50-day moving average, the strategy interprets this as weakening momentum.

The goal of this project is to test whether a simple momentum-based trading strategy can outperform a passive buy-and-hold approach over a given time period.