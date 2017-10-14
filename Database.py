# --- DATABASE QUERY METHODS --- #

import sqlite3
from sqlite3 import Error


class Database:

    def __init__(self, databaseFile = "payBob.sqlite"):
        try:
            self.databaseFile = databaseFile
            self.conn = sqlite3.connect(databaseFile)
        except Error as e:
            print(e)
        finally:
            self.conn.close()


    def create_table(conn, create_table_statement):
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_statement)
        except Error as e:
            print(e)
