import pytse_client as tse


# df = tse.download('اخابر')

df = tse.Ticker('اخابر')
print(df.shareholders)
