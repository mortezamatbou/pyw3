import mplfinance as mpf
import pandas as pd

dfo = pd.read_csv("./01-btc-demo.csv", skipinitialspace=True, parse_dates=True,
                  usecols=['Date', 'Open', 'High', 'Low', 'Close'])
dfo['Date'] = pd.to_datetime(dfo['Date'])

# --------------------------------------------------

dfo.set_index(keys='Date', inplace=True)
dfo.sort_index(ascending=True, inplace=True)


def heikin_ashi(df: pd.DataFrame):
    df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4

    idx = df.index.name
    df.reset_index(inplace=True)

    for i in range(0, len(df)):
        if i == 0:
            df.at[i, 'HA_Open'] = (df.iloc[i]['Open'] + df.iloc[i]['Close']) / 2
        else:
            df.at[i, 'HA_Open'] = (df.iloc[i - 1]['HA_Open'] + df.iloc[i - 1]['HA_Close']) / 2

    df['HA_High'] = df[['HA_Open', 'HA_Close', 'High']].max(axis=1)
    df['HA_Low'] = df[['HA_Open', 'HA_Close', 'Low']].min(axis=1)

    c = df.copy()[['Date', 'HA_Open', 'HA_High', 'HA_Low', 'HA_Close']]
    c.rename(columns={'HA_Open': 'Open', 'HA_High': 'High', 'HA_Low': 'Low', 'HA_Close': 'Close'}, inplace=True)

    if idx:
        df.set_index(idx, inplace=True)
        c.set_index(idx, inplace=True)

    return c


dfo.dropna(inplace=True)

data = heikin_ashi(dfo)
# mpf.plot(data, type='candle')

fig = mpf.figure(figsize=(12, 9))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

mpf.plot(dfo, type='candle', ax=ax1, axtitle='Candle stick', xrotation=0)
mpf.plot(data, type='candle', ax=ax2, axtitle='Heikin Ashi', xrotation=0)
mpf.show()
