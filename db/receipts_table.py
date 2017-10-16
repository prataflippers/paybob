def checkReciptsTable(self):
    checkCommand = "SELECT * FROM receipt;"
    arguments = ()
    cursor = self.conn.cursor()
    cursor.execute(checkCommand, arguments)

    rows = cursor.fetchall()

    if rows != []:
        return rows[0]
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
