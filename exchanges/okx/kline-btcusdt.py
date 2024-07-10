import requests
import time
from datetime import datetime
import mysql.connector
import pandas as pd
import numpy as np

# BTCUSDT
_from_ = 1533513600  # 2017-08-28
symbol = 'BTC-USDT'

intraday = []
tf = 400  # timeframe
resolution = 1
forward = 2600

segments = int((forward * 86400) / (tf * 60))
for i in range(segments):
    intraday.append(_from_)
    _from_ += tf * 60

backyard = mysql.connector.connect(
    host="localhost",
    user="testuser",
    password="testuser",
    database='backyard',
    port=3307
)
db = backyard.cursor()

ex_id = 1
pair_id = 1

j = 0

limit = 499
while True:
    for start in intraday:
        _from = "{}000".format(start)
        _to = "{}000".format(start + (tf * 60))
        url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={resolution}m&limit={limit}&startTime={_from}&endTime={_to}'
        url = f'https://www.okx.com/api/v5/market/history-mark-price-candles?instId={symbol}&confirm=1&bar=1m'
        uu = 'https://www.okx.com/api/v5/market/history-mark-price-candles?instId=BTC-USDT&confirm=1&bar=1Dutc&after=1583107200000'
        response = requests.get(url)
        res = response.json()
        print("from {} to {} :".format(datetime.fromtimestamp(start), datetime.fromtimestamp(start + (tf * 60))))
        if not res:
            print('NO DATA\n--------------------------------------------')
            continue

        df = pd.DataFrame(res, columns=['t', 'o', 'h', 'l', 'c', 'v', 'ct', 'bv', 'numOfTrade', 'takerBuyVolume',
                                        'TakerBaseBuyVolume', 'ig'])
        # print(df)
        # exit()
        for index, row in df.iterrows():
            sql = 'INSERT INTO klines1m(pair_id, ex_id, openTime, closeTime, o, h, l, c, v, numOfTrade) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = (
                pair_id, ex_id, row['t'], row['ct'], row['o'], row['h'], row['l'], row['c'],
                row['v'],
                row['numOfTrade'])
            db.execute(sql, values)
        backyard.commit()

        j += 1

        if j % 9 == 0:
            print('------ Sleep for 1 second --------')
            time.sleep(1)

    break
