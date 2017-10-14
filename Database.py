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


    def create_table(self, conn, create_table_statement):
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_statement)
        except Error as e:
            print(e)

    def setup(self):

        makeUserandIDtable = """CREATE TABLE IF NOT EXISTS user (
                                id Integer PRIMARY KEY AUTOINCREMENT,
                                username Text NOT NULL,
                                chatID Integer NOT NULL
                            );"""

        inline = "CREATE TABLE IF NOT EXISTS user (id Integer PRIMARY KEY AUTOINCREMENT, username Text NOT NULL, chatID Integer NOT NULL);"

        self.create_table(self.conn, makeUserandIDtable)
        # cursor = self.conn.cursor()
        # cursor.execute(makeUserandIDtable)

    def addUser(self, username, chatId):
        addUser = """INSERT INTO user(username, chatID)
                     VALUES (?, ?);"""

        user = (username, chatId,)

        cursor = self.conn.cursor()
        cursor.execute(addUser, user)


    def getChatID(self, name):

        selectCommand = "SELECT username FROM user WHERE username=?"
        arguments = (name,)

        cursor = self.conn.cursor()
        cursor.execute(selectCommand, arguments)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    # def getUsername(chatId):

def main():
    db = Database()
    db.setup()
    db.addUser("Suyash", 231)
    db.getChatID("Suyash")


if __name__ == '__main__':
    main()
