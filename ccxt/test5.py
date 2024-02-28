import ccxt
from zoneinfo import ZoneInfo
import datetime

exchange = ccxt.binance()
response = exchange.fetch_ohlcv('ADA/USDT', '1d', params={'price': 'index'}, limit=5)

for i in response:
    p = 'o:{o} h:{h} l:{l} c:{c}'.format(o=i[1], h=i[1], l=i[2], c=i[3])
    print(datetime.datetime.fromtimestamp(i[0] / 1000, tz=ZoneInfo('Asia/Tehran')), p)

# last1 = response[len(response)-1]
# last2 = response[len(response)-2]
# last3 = response[len(response)-3]
# print(datetime.datetime.fromtimestamp(last1[0] / 1000, tz=ZoneInfo('Asia/Tehran')), last1[1:])
# print(datetime.datetime.fromtimestamp(last2[0] / 1000, tz=ZoneInfo('Asia/Tehran')), last2[1:])
# print(datetime.datetime.fromtimestamp(last3[0] / 1000, tz=ZoneInfo('Asia/Tehran')), last3[1:])

# Convenience methods
# mark_klines = exchange.fetch_mark_ohlcv('ADA/USDT', '1m')
# last1 = mark_klines[-1]
# last2 = mark_klines[-2]
# last3 = mark_klines[-3]

# index_klines = exchange.fetch_index_ohlcv('ADA/USDT', '1d')
# last1 = index_klines[-1]
# last2 = index_klines[-2]
# last3 = index_klines[-3]

# 1707121980000,

# print(datetime.datetime.fromtimestamp(last1[0] / 1000, tz=ZoneInfo('Asia/Tehran')), last1[1:])
# print(datetime.datetime.fromtimestamp(last2[0] / 1000, tz=ZoneInfo('Asia/Tehran')), last2[1:])
# print(datetime.datetime.fromtimestamp(last3[0] / 1000, tz=ZoneInfo('Asia/Tehran')), last3[1:])
