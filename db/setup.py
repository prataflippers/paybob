import sqlite3
from sqlite3 import Error

def initialise(self, databaseFile = "payBob.sqlite"):
    try:
        self.databaseFile = databaseFile
        self.conn = sqlite3.connect(databaseFile)
    except Error as e:
        print(e)


def create_table(conn, create_table_statement):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_statement)
    except Error as e:
        print(e)
