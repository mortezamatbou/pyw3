import ccxt

ex = ccxt.binance()
data = ex.fetch_ohlcv(symbol='BTCUSDT', timeframe="5m", limit=3, params={'price': 'index'})
print(data)
