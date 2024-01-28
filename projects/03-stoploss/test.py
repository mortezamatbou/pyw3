amount = 1.279
buy = 20.500
price = buy

# for low-risk: stop_loss_percent = (4.8 to 5) * safe_line_percent
# stop_loss_percent = 33.36
stop_loss_percent = 20
# safe_line_percent = round(stop_loss_percent * 2, 2)
safe_line_percent = round(stop_loss_percent * 2, 2)
safe_sell_percent = round(stop_loss_percent + (safe_line_percent * 1), 2)

# safe_line_percent = 5.00
# stop_loss_percent = 30.36
# safe_sell_percent = round(stop_loss_percent + (safe_line_percent * 2), 2)
# safe_sell_percent = 80


total_buy = round(amount * buy, 5)
total_sell = 0

stop_loss_price = round(buy - ((buy * stop_loss_percent) / 100), 5)
safe_line_price = round(buy + ((buy * safe_line_percent) / 100), 5)

safe_line_sell_price = round((safe_line_price * safe_line_percent) / 100, 5)

print('[ORDER {} * {} = {}]'.format(price, amount, total_buy))
print("[AVAILABLE {} unit]".format(amount), end="\n\n")

print('[STOP LOSS] {percent}% -> {price}$'.format(percent=stop_loss_percent, price=stop_loss_price))

print('[SAFE LINE] {percent}%  -> {price}$'.format(percent=safe_line_percent, price=safe_line_price))
print('[SAFE LINE] safe sell percent -> {percent}%'.format(percent=safe_sell_percent), end="\n\n")

price = safe_line_price
print("[AVAILABLE {} unit]".format(amount))

safe_line_profit = round(((safe_line_price * amount) * safe_sell_percent) / 100, 5)
total_sell = round(total_sell + safe_line_profit, 5)
amount_val = round(amount * price, 5)
amount = round(amount - ((amount * safe_sell_percent) / 100), 5)
print('SELL {}% at price {}, total sell {} on balance {}'.format(safe_sell_percent, price, total_sell, amount_val))
print("AMOUNT {}, total price {}".format(amount, (amount * price)), end="\n\n")

price = stop_loss_price
print("[AVAILABLE {} unit]".format(amount))

total_sell = round(total_sell + (amount * price), 5)
amount = 0.00
print('SELL {}% at price {}, total sell {}'.format(100, price, total_sell))
print("AMOUNT {}, total price {}".format(amount, (amount * price)), end="\n\n")

# print("AMOUNT", amount, end="\n\n")
# print("SELL at {}, amount {}, total_price {}".format(price, amount, round((amount * price), 5)), end="\n\n")

print("--------------------------------------")
print("Total Buy", total_buy)
print("Total Sell", total_sell)

profit = round(((total_sell * 100) / total_buy) - 100, 4)
print("PROFIT {}%".format(profit))

print("--------------------------------------")
