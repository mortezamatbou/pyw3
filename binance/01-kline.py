import requests

market = 'BTCUSDT'
tick_interval = '1m'
limit = 1

startTime = '1715599740000'
endTime = '1715599800000'

url_spot = f'https://api.binance.com/api/v3/klines?symbol={market}&interval={tick_interval}&limit={limit}&startTime={startTime}&endTime={endTime}'
url_future = f'https://fapi.binance.com/fapi/v1/klines?symbol={market}&interval={tick_interval}&limit={limit}&startTime={startTime}&endTime={endTime}'
data = requests.get(url_future).content

print(data)
