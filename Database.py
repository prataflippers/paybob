import sqlite3
from sqlite3 import Error
from db.setup import initialise
from db.migrate import migrate
from db.users_table import addUser, getChatID, getUsername
from db.pendings_table import insertPending, getPending, getAllPending, deleteAllPending
from db.totals_table import owesToList, moneyOwed, addEntryToTotals, updateTotals, getTotalsEntryId
from db.history_queries import selfHistory, payingHistory, receivingHistory, transactionHistory, history
from db.receipts_table import checkReciptsTable, addReceipt, incrementReceipt, decrementReceipt, paidEverything
from db.totals_queries import owesMoneyTo, hasNotPaid

class Database:

    def __init__(self, databaseFile = "payBob.sqlite"):
        initialise(self, databaseFile = "payBob.sqlite")

    def setup(self):
        migrate(self)

    def insertPending(self, payer, payee, description, amount):
        insertPending(self, payer, payee, description, amount)

    def getPending(self, payer, payee):
        return getPending(self, payer, payee)

    def getAllPending(self, payee):
        return getAllPending(self, payee)

    def deleteAllPending(self, payee):
        return deleteAllPending(self, payee)

    def checkReciptsTable(self):
        return checkReciptsTable(self)

    def addUser(self, username, chatId):
        self.printTable("user")
        addUser(self, username, chatId)

    def getChatID(self, name):
        return getChatID(self, name)

    def getUsername(self, chatId):
        return getUsername(self, chatId)

    def selfHistory(self, username):
        return selfHistory(self, username)

    def owesToList(self, payer):
        return owesToList(self, payer)

    def moneyOwed(self, payer, payee):
        return moneyOwed(self, payer, payee)

    def addEntryToTotals(self, payer, payee, amount):
        addEntryToTotals(self, payer, payee, amount)

    def updateTotals(self, payer, payee, amount):
        updateTotals(self, payer, payee, amount)

    def getTotalsEntryId(self, payer, payee):
        return getTotalsEntryId(self, payer, payee)

    def payingHistory(self, username):
        return payingHistory(self, username)

    def receivingHistory(self, username):
        return receivingHistory(self, username)

    def addReceipt(self, payer, payee, description, amount):
        addReceipt(self, payer, payee, description, amount)

    def owesMoneyTo(self, username):
        return owesMoneyTo(self, username)

    def hasNotPaid(self, username):
        return hasNotPaid(self, username)

    def incrementReceipt(self, payerUsername, payeeUsername, description, amount):
        incrementReceipt(self, payerUsername, payeeUsername, description, amount)

    def decrementReceipt(self, payerUsername, payeeUsername, description, amount):
        decrementReceipt(self, payerUsername, payeeUsername, description, amount)

    def paidEverything(self, payerUsername, payeeUsername):
        paidEverything(self, payerUsername, payeeUsername)

    def history(self, payer):
        return history(self, payer)

    def transactionHistory(self, payer, payee):
        return transactionHistory(self, payer, payee)

    def printTable(self, tableName):
        selectAll = "SELECT * FROM {}".format(tableName)
        cursor = self.conn.cursor()
        cursor.execute(selectAll)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
