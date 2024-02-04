from cleandata import CleanData

obj = CleanData('./rawdata/EURUSD-1M.csv', 'EURUSD', '1M')
obj.update()

obj = CleanData('./rawdata/EURUSD-1W.csv', 'EURUSD', '1W')
obj.update()

obj = CleanData('./rawdata/EURUSD-1D.csv', 'EURUSD', '1D')
obj.update()

obj = CleanData('./rawdata/EURUSD-1h.csv', 'EURUSD', '1h')
obj.update()

obj = CleanData('./rawdata/EURUSD-30m.csv', 'EURUSD', '30m')
obj.update()

obj = CleanData('./rawdata/EURUSD-15m.csv', 'EURUSD', '15m')
obj.update()

obj = CleanData('./rawdata/EURUSD-5m.csv', 'EURUSD', '5m')
obj.update()

obj = CleanData('./rawdata/EURUSD-1m.csv', 'EURUSD', '1m')
obj.update()

obj = CleanData('./rawdata/EURUSD-30S.csv', 'EURUSD', '30S')
obj.update()

obj = CleanData('./rawdata/EURUSD-15S.csv', 'EURUSD', '15S')
obj.update()

obj = CleanData('./rawdata/EURUSD-5S.csv', 'EURUSD', '5S')
obj.update()

obj = CleanData('./rawdata/EURUSD-1S.csv', 'EURUSD', '1S')
obj.update()
