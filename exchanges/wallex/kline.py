import requests
import time
from datetime import datetime
import mysql.connector
import pandas as pd

# 100 request per second
# https://api.wallex.ir/v1/udf/history?symbol=BTCTMN&resolution=60&from=1654350171&to=1655502171
# 2024-06-12 10:00:00 1718173800
# 2024-06-12 11:00:00 1718177400

# symbol = 'BTCUSDT'
# symbol = 'TONTMN'
# symbol = 'BTCTMN'

# resolution = '1'
# _from = '1718173800'  # 2024-06-12 10:00:00 Asia/Tehran
# _to = '1718174100'  # 2024-06-12 10:05:00 Asia/Tehran

# resolution = '60'
# _from = '1718186400'  # 2024-06-12 10:00:00 Asia/Tehran
# _to = '1718190000'  # 2024-06-12 11:00:00 Asia/Tehran

# resolution = 'D'
# _from = '1577836800'  # 2018-01-01 00:00:00 Asia/Tehran
# _to = '1718190000'  # 2019-12-29 00:00:00 Asia/Tehran

# resolution = '1'
# _from = 1642491000  # 2024-06-12 10:00:00 Asia/Tehran
# _to = _from + 300  # 2024-06-12 10:05:00 Asia/Tehran
# _from = 1642404600  # 2024-06-12 10:00:00 Asia/Tehran
# _from = 1642231800  # 2024-06-12 10:00:00 Asia/Tehran
# _from = 1641713400  # 2024-06-12 10:00:00 Asia/Tehran
# _from = 1641706200  # 1400-10-19 2022-01-09 09:00:00 Asia/Tehran

# url = f'https://api.wallex.ir/v1/udf/history?symbol={symbol}&resolution={resolution}&from={_from}&to={_to}'
# response = requests.get(url).json()
# print(response)
# exit()

# _from_ = 1577824200 * (60 * 9)
# _to_ = 1577910600 * (60 * 10)
# _from_ = 1641706200
# _from_ = 1713817800  # TON
# _to_ = 1578601800

_from_ = 1610137800  # BTCTMN
j = 0

intraday = []
tf = 60  # timeframe
resolution = 1
forward_day = 10
segments = int((forward_day * 86400) / (tf * 60))
for i in range(segments):
    j += 1
    # f = datetime.fromtimestamp(_from_)
    # print(f, end=' ')
    # if j % 5 == 0:
    #     print("")
    intraday.append(_from_)
    _from_ += tf * 60

file = open(f'kline-genesis-candle-{symbol}-{tf}m.txt', 'w')
while True:
    for start in intraday:
        _from = start
        _to = _from + (tf * 60)
        url = f'https://api.wallex.ir/v1/udf/history?symbol={symbol}&resolution={resolution}&from={_from}&to={_to}'
        response = requests.get(url)

        txt = "from {} to {} :".format(datetime.fromtimestamp(_from), datetime.fromtimestamp(_to))
        print(txt)

        ex_id = 3
        pair_id = 1

        res = response.json()

        if res['s'] == 'no_data':
            print('[NO DATA]\n--------------------------------------------------------')
        else:
            print('[OK]\n--------------------------------------------------------')

        txt = txt + "\n" + response.text + "\n-------------------------------------\n"
        file.write(txt + "\n")

        time.sleep(1)
    break

# url = f'https://api.wallex.ir/v1/udf/history?symbol={symbol}&resolution={resolution}&from={_from}&to={_to}'
# response = requests.get(url).json()
# print(response)

"""
{
    "s": "ok",
    "t": [1718186400, 1718190000],
    "c": ["4019133342.0000000000000000", "4014507498.0000000000000000"],
    "o": ["3999999999.0000000000000000", "4019133346.0000000000000000"],
    "h": ["4023066112.0000000000000000", "4031118548.0000000000000000"],
    "l": ["3999999999.0000000000000000", "4013507464.0000000000000000"],
    "v": ["0.2669160000000000", "0.2653340000000000"]
}

"""
