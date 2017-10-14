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
        self.makeUsersTable()
        self.makeReceiptsTable()
        self.makeTotalsTable()

    def makeUsersTable(self):
        makeUserandIDtable = """CREATE TABLE IF NOT EXISTS user (
                                id Integer PRIMARY KEY AUTOINCREMENT,
                                username Text NOT NULL UNIQUE,
                                chatID Integer NOT NULL UNIQUE
                            );"""
        self.create_table(self.conn, makeUserandIDtable)


    def makeReceiptsTable(self):
        makeReceipts = """CREATE TABLE IF NOT EXISTS receipt (
                            id Integer PRIMARY KEY AUTOINCREMENT,
                            payer Integer NOT NULL,
                            payee Integer NOT NULL,
                            description Text,
                            amount Float NOT NULL
                            );"""
        self.create_table(self.conn, makeReceipts)


    def makeTotalsTable(self):
        makeTotals = """CREATE TABLE IF NOT EXISTS total (
                                id Integer PRIMARY KEY AUTOINCREMENT,
                                payer Integer NOT NULL,
                                payee Integer NOT NULL,
                                amount Float NOT NULL
                    );"""
        self.create_table(self.conn, makeTotals)

#=============================== USER COMMANDS ================================#

    def addUser(self, username, chatId):
        addUser = "INSERT INTO user(username, chatID) VALUES (?, ?);"


        arguments = (username, chatId,)

        cursor = self.conn.cursor()
        cursor.execute(addUser, arguments)
        self.conn.commit()


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
#===============================TRANSACTION COMMANDS===========================#

    def moneyOwed(self, payer, payee):

        findEntry = "SELECT amount FROM total WHERE payer=? AND payee=?"

        cursor = self.conn.cursor()
        arguments = (payer, payee)
        cursor.execute(findEntry, arguments)
        rows = cursor.fetchall()

        if rows != []:
            return rows[0][0]
        else:

            cursor = self.conn.cursor()
            arguments = (payee, payer)
            cursor.execute(findEntry, arguments)

            rows = cursor.fetchall()

            if rows != []:
                return -1 * rows[0][0]
            else:
                return 0

    def addEntryToTotals(self, payer, payee, amount):
        addCommand = "INSERT INTO total(payer, payee, amount) VALUES (?, ?, ?);"
        arguments = (payer, payee, amount)
        cursor = self.conn.cursor()
        cursor.execute(addCommand, arguments)

        self.conn.commit()

    # Used when payer pays payee x amount. so it reduces how much the payee owes
    def updateTotals(self, payer, payee, amount):
        updateCommand = "UPDATE total SET amount = amount + ? WHERE id = ?;"
        entryId = self.getTotalsEntryId(payer, payee)
        cursor = self.conn.cursor()

        if (entryId != None):
            arguments = (amount, entryId)
            cursor.execute(updateCommand, arguments)
        else:
            entryId = self.getTotalsEntryId(payee, payer)
            if (entryId != None):
                arguments = (-1 * amount, entryId)
                cursor.execute(updateCommand, arguments)
            # else:
                #NO Entry exists between the two people

        self.conn.commit()


    def getTotalsEntryId(self, payer, payee):
        findEntryinTotals = "SELECT id FROM total WHERE payer=? AND payee=?"
        arguments = (payer, payee)
        cursor = self.conn.cursor()
        cursor.execute(findEntryinTotals, arguments)
        rows = cursor.fetchall()

        if rows != []:
            return rows[0][0]
        else:
            return None


    # When: 1. Payer pays back payee.
    #       2. Payer lends payee money
    def addReceipt(self, payer, payee, description, amount):

        # Make entry in the receipt table
        makeReceipt = "INSERT INTO receipt(payer, payee, description, amount) VALUES (?, ?, ?, ?);"
        arguments = (payer, payee, description, amount)
        cursor = self.conn.cursor()
        cursor.execute(makeReceipt, arguments)

        # Check if a totals entry exists between the two users
        entryId = -1
        entryFound = self.getTotalsEntryId(payer, payee)
        if entryFound != None:
            entryId = entryFound
        else:
            entryFound = self.getTotalsEntryId(payee, payer)
            if entryFound != None:
                entryId = entryFound

        entryExists = (entryId != -1)
        print(entryExists)
        if entryExists:
            self.updateTotals(payer, payee, amount)
        else:
            self.addEntryToTotals(payer, payee, amount)

        self.conn.commit()

    def printTable(self, tableName):
        selectAll = "SELECT * FROM {}".format(tableName)
        cursor = self.conn.cursor()
        cursor.execute(selectAll)
        rows = cursor.fetchall()
        for row in rows:
            print row


    #returns a list of all the people the 'username' owes money to and how much
    #[(Username, Amount)]
    def owesMoneyTo(self, username):
        cursor = self.conn.cursor()
        arguments = (username,)
        list = []

        filterEntries = "SELECT payer, amount FROM total WHERE payee=? AND amount > 0"
        cursor.execute(filterEntries, arguments)
        rows = cursor.fetchall()
        for row in rows:
            list.append((str(row[0]), row[1]))

        filterEntries = "SELECT payee, amount FROM total WHERE payer=? AND amount < 0"
        cursor.execute(filterEntries, arguments)
        rows = cursor.fetchall()
        for row in rows:
            list.append((row[0], -1 * row[1]))

        print(username + " owes the following people money")
        print(list)
        print("  ")

    #returns a list of all the people that owe 'username' money and how much they owe
    def hasNotPaid(self, username):
        cursor = self.conn.cursor()
        arguments = (username,)
        list = []

        filterEntries = "SELECT payer, amount FROM total WHERE payee=? AND amount < 0"
        cursor.execute(filterEntries, arguments)
        rows = cursor.fetchall()
        for row in rows:
            list.append((str(row[0]), -1 * row[1]))

        filterEntries = "SELECT payee, amount FROM total WHERE payer=? AND amount > 0"
        cursor.execute(filterEntries, arguments)
        rows = cursor.fetchall()
        for row in rows:
            list.append((str(row[0]), row[1]))

        print("THE FOLLOWING PEOPLE OWE " + username + " MONEY")
        print(list)
        print("  ")

#==============================================================================#

def main():

    # TESTS
    db = Database()
    db.setup()
    db.addUser("Suyash", 231)
    print(db.getChatID("Suyash"))
    print(db.getUsername(231))
    print(db.getChatID("Suysdash"))
    print(db.getUsername(12223))
    # db.addEntryToTotals("Suyash", "Haozhe", 396.23)
    print(db.moneyOwed("Suyash", "Haozhe"))
    print(db.moneyOwed("Haozhe", "Suyash"))
    print(db.moneyOwed("Shitian", "Suyash"))
    print(db.moneyOwed("Haozhe", "Junkai"))
    db.addReceipt("Haozhe", "Junkai", "Firecracker Chicken", 4.50)
    db.addReceipt("Haozhe", "Junkai", "Dabao", 4.50)
    db.addReceipt("Junkai", "Haozhe", "Dabao", 60)
    db.addReceipt("Haozhe", "Junkai", "Dabao", 200)


    db.owesMoneyTo("Haozhe")
    db.owesMoneyTo("Junkai")
    db.owesMoneyTo("Suyash")
    db.hasNotPaid("Haozhe")
    db.hasNotPaid("Junkai")
    db.hasNotPaid("Suyash")

    db.printTable("receipt")
    print("  ")
    db.printTable("total")

if __name__ == '__main__':
    main()
