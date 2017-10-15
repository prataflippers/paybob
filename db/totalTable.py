# Returns list of tuples (user, amount) whom payee owes money to
def owesToList(self, payer):

    findEntry = "SELECT * FROM total WHERE amount > 1.0 AND payee=?"
    cursor = self.conn.cursor()
    arguments = (payer,)
    cursor.execute(findEntry, arguments)
    rows = cursor.fetchall()

    listOfLoaners = []
    for row in rows:
        print(row[1])
        listOfLoaners.append((row[1], row[3]))
    return listOfLoaners

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
