import requests
import time
from datetime import datetime
import mysql.connector
import pandas as pd
import numpy as np

# ADAIRT
_from_ = 1708374600  # 2021-01-21 00:00:00
symbol = 'ADAIRT'

intraday = []
tf = 300  # timeframe
resolution = 1
forward = 120

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

ex_id = 4
pair_id = 10

j = 0

while True:
    for start in intraday:
        _from = start
        _to = _from + (tf * 60)
        url = f'https://api.nobitex.ir/market/udf/history?symbol={symbol}&resolution={resolution}&from={_from}&to={_to}'
        response = requests.get(url)
        res = response.json()

        j += 1

        if j % 5 == 0:
            time.sleep(1)

        print("from {} to {} :".format(datetime.fromtimestamp(_from), datetime.fromtimestamp(_to)))
        if res['s'] == 'no_data':
            print('NO DATA\n--------------------------------------------')
            continue

        t = pd.Series(res['t'], dtype=int)
        po = pd.Series(res['o'])
        ph = pd.Series(res['h'])
        pl = pd.Series(res['l'])
        pc = pd.Series(res['c'])
        volume = pd.Series(res['v'])
        numOfTrade = np.zeros(t.shape, dtype=int)

        df = pd.DataFrame({'t': t, 'o': po, 'h': ph, 'l': pl, 'c': pc, 'v': volume, 'numOfTrade': numOfTrade})

        print(df)
        exit()

        for index, row in df.iterrows():
            sql = 'INSERT INTO klines1m(pair_id, ex_id, openTime, closeTime, o, h, l, c, v, numOfTrade)' \
                  ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = (
                pair_id, ex_id, row['t'], (row['t'] + (resolution * 60)), row['o'], row['h'], row['l'], row['c'],
                row['v'],
                row['numOfTrade'])
            db.execute(sql, values)
        backyard.commit()

    break
