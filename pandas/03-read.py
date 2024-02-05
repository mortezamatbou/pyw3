import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('BTCUSDT_candle_sample.csv')
# df = df[0:5][['date', 'symbol', 'open', 'high', 'low', 'close']]
# df = df[0:][['open', 'high', 'low', 'close']]

# df = df[0:10][['high', 'close']]

# df.plot()
# plt.show()

# print(df.head(10))
# print(df.tail(10))
print(df.info())

