import requests

url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1M&startTime=1499990400000&limit=1'
data = requests.get(url).json()

# Binance launched July 2017
# Find first month from 2017-07-01
# From first month, find first week
# From first week, find first day
# From first day, find first 1m kline data

"""
result
[
    [
        1501545600000, ***
        "4261.48000000",
        "4745.42000000",
        "3400.00000000",
        "4724.89000000",
        "10015.64027200",
        1504223999999, ***
        "42538297.66482722",
        69180,
        "4610.01943100",
        "19419232.11660334",
        "0"
    ]
]
"""

print(data)
