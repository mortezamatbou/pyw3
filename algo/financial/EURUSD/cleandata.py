import csv
import os
from database import DB
from dotenv import load_dotenv


class CleanData:

    def __init__(self, csv_file_path, symbol, tf):
        load_dotenv(os.path.abspath('../../../.env'))
        file = open(os.path.abspath(csv_file_path), 'rt')
        self.csv_data = csv.reader(file)
        self.symbol = symbol
        self.tf = tf
        self.db = DB()

    def update(self):
        headers = next(self.csv_data)
        headers = [x.strip().lower() for x in headers]

        val = []
        for row in self.csv_data:
            date = row[headers.index('date')].replace('.', '-')
            time = (row[headers.index('time')] + ":00") \
                if self.tf not in ['1S', '5S', '15S', '30S'] \
                else row[headers.index('time')]

            d = "{} {}".format(date, time)
            o = float(row[headers.index('o')])
            h = float(row[headers.index('h')])
            l = float(row[headers.index('l')])
            c = float(row[headers.index('c')])
            vol = float(row[headers.index('v')])
            val.append((d, self.symbol, o, h, l, c, vol, self.tf))

        # sql = "DELETE FROM pairs WHERE sym='{}' AND tf='{}'".format(self.symbol, self.tf)
        # self.db.query(sql)
        sql = 'INSERT INTO pairs(d, sym, o, h, l, c, vol, tf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        self.db.insert_many(sql, val)
