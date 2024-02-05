import pandas as pd
import mplfinance as mpf
import yfinance as yf  # (for the dataset)

# Define the stock symbol and date range
stock_symbol = "AAPL"  # Example: Apple Inc.
start_date = "2022-01-01"
end_date = "2022-01-05"

# Load historical data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

print(stock_data.index.values.tolist())

# plot
# mpf.plot(stock_data, type='candle')
