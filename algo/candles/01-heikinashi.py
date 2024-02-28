import mplfinance as mpf
import pandas as pd
import numpy as np

# data = {
#     "Date": [pd.Timestamp("2024-02-14"), pd.Timestamp("2024-02-15"), pd.Timestamp("2024-02-16"),
#              pd.Timestamp("2024-02-17"), pd.Timestamp("2024-02-18"), pd.Timestamp("2024-02-19"),
#              pd.Timestamp("2024-02-20"), pd.Timestamp("2024-02-21")],
#     "Open": [6, 7, 8, 9, 10, 11, 12, 13],
#     "High": [10, 50, 25, 30, 13, 15, 16, 16],
#     "Low": [11, 12, 13, 14, 15, 8, 10, 12],
#     "Close": [16, 17, 18, 19, 20, 21, 25, 22],
# }

# df = pd.DataFrame(data)
# df.set_index(keys="Date", inplace=True)

# df = pd.read_csv("./01-btc-sample-1D.csv", skipinitialspace=True, parse_dates=True,
#                  usecols=['Date', 'Open', 'High', 'Low', 'Close', 'Volume BTC', 'Volume USDT'])
# df['Date'] = pd.to_datetime(df['Date'])

# --------------------------------------------------
# df = pd.read_csv("./01-btc-sample-1h.csv", skipinitialspace=True, parse_dates=True,
#                  usecols=['Date', 'Unix Timestamp', 'Open', 'High', 'Low', 'Close'])
#
# df['Date'] = pd.to_datetime(df['Unix Timestamp'], unit='s')
# --------------------------------------------------

df = pd.read_csv("./01-EURUSD-sample-5m.csv", skipinitialspace=True, parse_dates=True,
                 usecols=['Date', 'Time', 'Open', 'High', 'Low', 'Close'])
df['Date'] = pd.to_datetime(df['Date'] + " " + df['Time'])
# --------------------------------------------------

df.set_index(keys='Date', inplace=True)
df.sort_index(ascending=True, inplace=True)

"""

HA [Close] : (Open0 + High0 + Low0 + Close0) / 4
HA [Open] : (Open-1 + Close-1) / 2
HA [High] : MAX(High0, HA Open0, HA Close0)
HA [Low] : MIN(Low0, HA Open0, HA Close0)

Open0 etc. = Values from the current period
Open-1 etc. = Values from the prior period
HA = Heikin-Ashi
"""
df['hClose'] = df[['Open', 'High', 'Low', 'Close']].mean(axis=1)
df['hOpen'] = (df['Open'].shift(1) + df['Close'].shift(1)) / 2
df['hHigh'] = df[['High', 'hOpen', 'hClose']].apply(np.max, axis=1)
df['hLow'] = df[['Low', 'hOpen', 'hClose']].apply(np.min, axis=1)

df.dropna(inplace=True)

data = df[["Time", "Open", "High", "Low", "Close"]]
# print(data[''])
# show = data.loc['2024-01-28 00:00:00': '2024-02-02 23:55:00']
# mpf.plot(show, type='candle',
#          hlines=dict(hlines=[show.iloc[52]['Low']], colors=['g'], linestyle='-', alpha=0.4, linewidths=(0.5,)))
mpf.plot(data, type='candle')
