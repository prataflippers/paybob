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
        self.makeUsers()
        self.makeReceipts()
        self.makeTotals()

    def makeUsers(self):
        makeUserandIDtable = """CREATE TABLE IF NOT EXISTS user (
                                id Integer PRIMARY KEY AUTOINCREMENT,
                                username Text NOT NULL,
                                chatID Integer NOT NULL
                            );"""
        self.create_table(self.conn, makeUserandIDtable)


    def makeReceipts(self):
        makeReceipts = ""
        self.create_table(self.conn, makeReceipts)


    def makeTotals(self):
        makeTotals = ""
        self.create_table(self.conn, makeTotals)

#=============================== USER COMMANDS ================================#

    def addUser(self, username, chatId):
        addUser = """INSERT INTO user(username, chatID)
                     VALUES (?, ?);"""

        arguments = (username, chatId,)

        cursor = self.conn.cursor()
        cursor.execute(addUser, arguments)


    def getChatID(self, name):

        selectCommand = "SELECT chatID FROM user WHERE username=?"
        arguments = (name,)

        cursor = self.conn.cursor()
        cursor.execute(selectCommand, arguments)

        rows = cursor.fetchall()

        if rows != []:
            return rows[0][0]
        else:
            return None

    def getUsername(self, chatId):

        selectCommand = "SELECT username FROM user WHERE chatID=?"
        arguments = (chatId,)

        cursor = self.conn.cursor()
        cursor.execute(selectCommand, arguments)

        rows = cursor.fetchall()

        if rows != []:
            return rows[0][0]
        else:
            return None

#==============================================================================#

    def makeReceipt(payerUsername, payeeUsername, amount, description):
        print("")

def main():

    # TESTS
    db = Database()
    db.setup()
    db.addUser("Suyash", 231)
    print(db.getChatID("Suyash"))
    print(db.getUsername(231))
    print(db.getChatID("Suysdash"))
    print(db.getUsername(12223))


if __name__ == '__main__':
    main()
