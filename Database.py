import sqlite3
from sqlite3 import Error
from db.databaseSetup import initialise, create_table, setup
from db.databaseCreateTables import usersTable, receiptsTable, pendingTable, totalsTable
from db.userTable import addUser, getChatID, getUsername
from db.pendingTable import insertPending, getPending, getAllPending, deleteAllPending
from db.totalTable import owesToList, moneyOwed, addEntryToTotals, updateTotals, getTotalsEntryId
from db.historyQueries import selfHistory, payingHistory, receivingHistory, transactionHistory, history
from db.receiptTable import checkReciptsTable, addReceipt, incrementReceipt, decrementReceipt, paidEverything
from db.totalsQuery import owesMoneyTo, hasNotPaid

class Database:

    def __init__(self, databaseFile = "payBob.sqlite"):
        initialise(self, databaseFile = "payBob.sqlite")

    def create_table(self, conn, create_table_statement):
        create_table(self, conn, create_table_statement)

    def setup(self):
        setup(self)

    def makeUsersTable(self):
        usersTable(self)

    def makeReceiptsTable(self):
        receiptsTable(self)

    def makePendingTable(self):
        pendingTable(self)

    def makeTotalsTable(self):
        totalsTable(self)

    def insertPending(self, payer, payee, description, amount):
        insertPending(self, payer, payee, description, amount)

    def getPending(self, payer, payee):
        getPending(self, payer, payee)

    def getAllPending(self, payee):
        getAllPending(self, payee)

    def deleteAllPending(self, payee):
        deleteAllPending(self, payee)

    def checkReciptsTable(self):
        checkReciptsTable(self)

    def addUser(self, username, chatId):
        addUser(self, username, chatId)

    def getChatID(self, name):
        getChatID(self, name)

    def getUsername(self, chatId):
        getUsername(self, chatId)

    def selfHistory(self, username):
        selfHistory(self, username)

    def owesToList(self, payer):
        owesToList(self, payer)

    def moneyOwed(self, payer, payee):
        moneyOwed(self, payer, payee)

    def addEntryToTotals(self, payer, payee, amount):
        addEntryToTotals(self, payer, payee, amount)

    def updateTotals(self, payer, payee, amount):
        updateTotals(self, payer, payee, amount)

    def getTotalsEntryId(self, payer, payee):
        getTotalsEntryId(self, payer, payee)

    def payingHistory(self, username):
        payingHistory(self, username)

    def receivingHistory(self, username):
        receivingHistory(self, username)

    def addReceipt(self, payer, payee, description, amount):
        addReceipt(self, payer, payee, description, amount)

    def owesMoneyTo(self, username):
        owesMoneyTo(self, username)

    def hasNotPaid(self, username):
        hasNotPaid(self, username)

    def incrementReceipt(self, payerUsername, payeeUsername, description, amount):
        incrementReceipt(self, payerUsername, payeeUsername, description, amount)

    def decrementReceipt(self, payerUsername, payeeUsername, description, amount):
        decrementReceipt(self, payerUsername, payeeUsername, description, amount)

    def paidEverything(self, payerUsername, payeeUsername):
        paidEverything(self, payerUsername, payeeUsername)

    def history(self, payer):
        history(self, payer)

    def transactionHistory(self, payer, payee):
        transactionHistory(self, payer, payee)

    def printTable(self, tableName):
        selectAll = "SELECT * FROM {}".format(tableName)
        cursor = self.conn.cursor()
        cursor.execute(selectAll)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
