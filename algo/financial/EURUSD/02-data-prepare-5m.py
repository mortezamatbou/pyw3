import csv
import mysql.connector
import os

from dotenv import load_dotenv

'''
This file don't handle exception
'''

exit()

load_dotenv(os.path.abspath('../../../.env'))

mydb = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE')
)
db = mydb.cursor()

# load csv file and loop
file = open(os.path.abspath('./rawdata/EURUSD-5m.csv'), 'rt')
csv_data = csv.reader(file)

sym = 'EURUSD'
headers = next(csv_data)
headers = [x.strip().lower() for x in headers]

val = []
for row in csv_data:
    date = row[headers.index('date')].replace('.', '-')
    time = row[headers.index('time')] + ":00"
    d = "{} {}".format(date, time)
    o = float(row[headers.index('o')])
    h = float(row[headers.index('h')])
    l = float(row[headers.index('l')])
    c = float(row[headers.index('c')])
    vol = float(row[headers.index('v')])
    val.append((d, sym, o, h, l, c, vol, "5m"))

db.execute("DELETE FROM pairs WHERE sym='EURUSD' AND tf='5m'")
sql = 'INSERT INTO pairs(d, sym, o, h, l, c, vol, tf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
o = db.executemany(sql, val)

mydb.commit()
print('EURUSD in 5m timeframe has been updated')
