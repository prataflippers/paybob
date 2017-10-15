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
        self.makePendingTable()

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

    def makePendingTable(self):
        makePending = """CREATE TABLE IF NOT EXISTS pending (
                            id Integer PRIMARY KEY AUTOINCREMENT,
                            payer Integer NOT NULL,
                            payee Integer NOT NULL,
                            description Text,
                            amount Float NOT NULL
                        );"""
        self.create_table(self.conn, makePending)

    def insertPending(self, payer, payee, description, amount):
            makeReceipt = "INSERT INTO receipt(payer, payee, description, amount) VALUES (?, ?, ?, ?);"
            arguments = (payer, payee, description, amount)
            cursor = self.conn.cursor()
            cursor.execute(makeReceipt, arguments)

    def getPending(self, payer, payee):
        getPending = "SELECT * FROM pending WHERE payer=? AND payee=?;"
        arguments = (payer, payee)
        cursor = self.conn.cursor()
        cursor.execute(makeReceipt, arguments)

        rows = cursor.fetchall()
        list[]
        if rows != []:
            for row in rows:
                list.append(str(row))
        else:
            return None

        return list

    def getAllPending(self, payee):
        getPending = "SELECT * FROM pending WHERE payee=?;"
        arguments = (payee)
        cursor = self.conn.cursor()
        cursor.execute(makeReceipt, arguments)

        rows = cursor.fetchall()

        list[]
        if rows != []:
            for row in rows:
                list.append(str(row))
        else:
            return None

        return list


    def checkReciptsTable(self):
        checkCommand = "SELECT * FROM receipt;"
        arguments = ()
        cursor = self.conn.cursor()
        cursor.execute(checkCommand, arguments)

        rows = cursor.fetchall()

        if rows != []:
            print(rows[0])
        else:
            return None

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

    #selfHistory returns a list of [description, othersName, amount]
    #[othersName, description, amount(positive for receiving, negative for  giving)]
    def selfHistory(self, username):
         selectCommand = "SELECT * FROM receipt WHERE payer=? OR payee =?"
         arguments = (username, username)

         cursor = self.conn.cursor()
         cursor.execute(selectCommand, arguments)

         rows = cursor.fetchall()
         list = []
         if rows != []:
             for row in rows:
                 if row[1] == username:
                     list.append((str(row[2]), str(row[3]), row[4]))
                 else:
                     amount = -row[4]
                     list.append((str(row[1]), str(row[3]), amount))

         else:
             return None

         return list
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

    #return type: [(paidTo, Description, Amount)]
    #username is the person giving the money
    def payingHistory(self, username):
        payingCommand = "SELECT * FROM receipt WHERE payer=?;"

        arguments = (username,)

        cursor = self.conn.cursor()
        cursor.execute(payingCommand, arguments)
        rows = cursor.fetchall()

        list = []
        if rows != []:
            for row in rows:
                    list.append((str(row[2]), str(row[3]), row[4]))
        else:
            return None
        return list

    #return type: [(receiveFrom, Description, Amount)]
    #username is the person reciving the money
    def receivingHistory(self, username):
        receivingCommand = "SELECT * FROM receipt WHERE payee=?;"

        arguments = (username,)

        cursor = self.conn.cursor()
        cursor.execute(receivingCommand, arguments)
        rows = cursor.fetchall()

        list = []
        if rows != []:
            for row in rows:
                    list.append((str(row[1]), str(row[3]), row[4]))
        else:
            return None
        return list


    # def transactionHistory(payerUsername, payeeUsername):
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
            print(row)


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

    #when the person who owed now owes more i.e. payer gives money to payee
    def incrementReceipt(self, payerUsername, payeeUsername, description, amount):
        self.addReceipt(payerUsername, payeeUsername, description, amount);

    #when the person who owes now owes less i.e. payee returns some money
    def decrementReceipt(self, payerUsername, payeeUsername, description, amount):
        self.addReceipt(payeeUsername, payerUsername, description, amount)

    #clears the receipts between the payer and payee
    def paidEverything(self, payerUsername, payeeUsername):
        pay = "DELETE FROM receipt WHERE (payer=? AND payee=?) OR (payer=? AND payee=?);"
        arguments = (payerUsername, payeeUsername, payeeUsername, payerUsername);
        cursor = self.conn.cursor()
        cursor.execute(pay, arguments)

    #returns a list of transactions between payer and payee.
    #the amount is positive if payer paid and negative if payee paid
    def transactionHistory(self, payer, payee):
        cursor = self.conn.cursor()
        filterEntries = "SELECT id, description, amount FROM receipt WHERE payer=? AND payee=?"
        arguments = (payer, payee)
        list = []

        cursor.execute(filterEntries, arguments)
        rows = cursor.fetchall()
        for row in rows:
            list.append((row[0], str(row[1]), row[2]))

        filterEntries = "SELECT id, description, amount FROM receipt WHERE payer=? AND payee=?"
        arguments = (payee, payer)
        cursor.execute(filterEntries, arguments)
        rows = cursor.fetchall()
        for row in rows:
            list.append((row[0], str(row[1]), -1 * row[2]))

        sorted_list = sorted(list, key=lambda x: x[0])
        list_without_ids = (map((lambda x: (x[1], x[2])) , sorted_list))

        print("These are the transactions between " + payer + " and " + payee)
        print(list_without_ids)
        print("  ")
        return list_without_ids

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
    print(" ")
    db.paidEverything("Haozhe", "Shitian")
    print("  ")

    db.transactionHistory("Haozhe", "Junkai")

    print(" ")
    db.printTable("total")


if __name__ == '__main__':
    main()
