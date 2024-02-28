import datetime

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

data = {}

start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(2020, 1, 1)
ticker = yf.download('IBM', start=start_date, end=end_date)

data['Price'] = ticker['Adj Close']
data = pd.DataFrame(data)

data['Short SMA'] = data['Price'].rolling(window=50).mean()
data['Long SMA'] = data['Price'].rolling(window=200).mean()
data = data.dropna()

plt.figure(figsize=(12, 6))
plt.plot(data['Price'], label="Stock Price", color="black")
plt.plot(data['Short SMA'], label="Short MA", color="red")
plt.plot(data['Long SMA'], label="Long MA", color="orange")
plt.title("Simple Moving Average (MA) Indicator")
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
