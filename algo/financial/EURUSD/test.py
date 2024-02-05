import pandas as pd
import mplfinance as mpf
import yfinance as yf  # (for the dataset)

data = pd.read_csv('./rawdata/EURUSD-temp.csv', index_col=0, parse_dates=True)
data.index.name = 'Date'

start_date = '2002-01-01'
end_date = '2010-01-01'

mpf.plot(data.loc[start_date:end_date], type='candle')

# data = pd.read_csv('./rawdata/EURUSD-5m.csv', index_col=0, parse_dates=True)
# data.index.name = 'Date'
# mpf.plot(data.loc['2023.06.02':'2023.06.03'], type='renko')

# 1.0735
