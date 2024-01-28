class Order:
    __sell_limit, __sell_percent, __sell_amount = 0, 0, 0
    stop_loss_percent = 0
    safe_target_price = 0

    def __init__(self, amount, price, stop_loss_price, commission=0):
        self.amount = round(amount, 3)
        self.price = round(price, 3)
        self.stop_loss_price = round(stop_loss_price, 3)
        self.stop_loss_percent = round(self.price - ((self.stop_loss_price * 100) / self.price), 2)
        self.commission = commission

        self.total_price = round(self.amount * self.price, 3)

        if self.price > self.stop_loss_price:
            # self.stop_loss_percent = self.stop_loss_percent * 1
            self.safe_target_price = round(self.price + self.stop_loss_price, 3)

    def add_target(self, limit, percent=0, amount=0):
        self.__sell_limit = limit
        self.__sell_percent = percent
        self.__sell_amount = amount

    # result type is in amount price or percent
    def get_buy_stop_diff(self):
        diff_price = round(self.total_price - (self.amount * self.stop_loss_price), 3)
        return diff_price

    def get_safe_price(self):
        safe_total_price = round((self.price + (self.get_buy_stop_diff() * 2)) * self.amount, 3)
        return safe_total_price

    def get_safe_percent(self):
        safe_price = self.get_safe_price()
        target_percent = self.stop_loss_percent
        percent = round((safe_price * target_percent) / 100, 2)
        total_price = round((safe_price * percent) / 100, 3)
        result = {'price': safe_price, 'percent': percent, 'total_price': total_price}
        return result

    # return info as string
    def print_info(self):
        s1_txt = "[--Buy info--] Amount({amount}), Price ({price})$. Total price ({total_price})\n"
        s1 = s1_txt.format(amount=self.amount, price=self.price, total_price=self.total_price)

        s2_txt = "[--Diff info--] Diff price({diff_price})$, Diff percent ({percent}%)\n"
        s2 = s2_txt.format(diff_price=self.get_buy_stop_diff(), percent=self.stop_loss_percent)

        s3_txt = "[--Safe info--] First safe target ({safe_target})$, Sell ({percent})%, Amount({amount})%\n"
        sell_amount = round(self.total_price - (self.amount * self.amount), 3)
        s3 = s3_txt.format(safe_target=self.safe_target_price, percent=self.stop_loss_percent, amount=sell_amount)

        txt = s1 + s2 + s3
        return txt


# order = Order(amount=1.277, price=20.550, stop_loss_price=14.298)
order = Order(amount=1, price=100.00, stop_loss_price=95.00)

safe_percent = order.get_safe_percent()

print("safe price", safe_percent['price'])
print("sell percent", safe_percent['percent'])
print("sell", safe_percent['total_price'])
