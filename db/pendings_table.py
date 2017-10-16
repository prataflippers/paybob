def insertPending(self, payer, payee, description, amount):
    makeReceipt = "INSERT INTO pending(payer, payee, description, amount) VALUES (?, ?, ?, ?);"
    arguments = (payer, payee, description, amount)
    cursor = self.conn.cursor()
    cursor.execute(makeReceipt, arguments)
    self.conn.commit()

def getPending(self, payer, payee):
    getPending = "SELECT * FROM pending WHERE payer=? AND payee=?;"
    arguments = (payer, payee)
    cursor = self.conn.cursor()
    cursor.execute(getPending, arguments)
    self.printTable("pending")

    rows = cursor.fetchall()
    list = []
    if rows != []:
        for row in rows:
            list.append(row)
    else:
        return None
    return list

def getAllPending(self, payee):
    getPending = "SELECT * FROM pending WHERE payee=?;"
    arguments = (payee,)
    cursor = self.conn.cursor()
    cursor.execute(getPending, arguments)

    rows = cursor.fetchall()

    list = []
    if rows != []:
        for row in rows:
            list.append(row)
    else:
        return None

    self.conn.commit()
    return list

def deleteAllPending(self, payee):
    deleteQuery = "DELETE FROM pending WHERE payee=?;"
    arguments = (payee,)
    cursor = self.conn.cursor()
    cursor.execute(deleteQuery, arguments)
    self.conn.commit()
