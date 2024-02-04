import mysql.connector
import os


class DB:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE')
        )
        self.db = self.mydb.cursor()

    def insert(self, sql, val):
        pass

    def query(self, sql):
        self.db.execute(sql)

    def insert_many(self, sql, val):
        try:
            self.db.executemany(sql, val)
            self.mydb.commit()
        except mysql.connector.errors.DataError:
            print("OOOOPS")
            print(val)

