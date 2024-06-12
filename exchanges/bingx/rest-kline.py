import requests

"""
limit      default is 500 maximum 1440
startTime  unit:millisecond
endTime    unit:millisecond
"""
URL = "https://open-api.bingx.com/openApi/swap/v3/quote/klines?symbol=BTC-USDT&interval=1h&limit=10&startTime=1718064000000"
data = requests.get(URL).json()

print(data)

"""
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "open": "67494.5",
      "close": "67060.3",
      "high": 67645.0,
      "low": 66849.1,
      "volume": 2961.29,
      "time": 1718096400000
    },
    {
      "open": 69529.0,
      "close": 69411.0,
      "high": 69571.8,
      "low": 69398.9,
      "volume": 487.52,
      "time": 1718064000000
    }
  ]
}

"""

