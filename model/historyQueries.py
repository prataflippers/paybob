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
                 amount = -1 * row[4]
                 list.append((str(row[1]), str(row[3]), amount))
     else:
         return None

     return list

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

def history(self, payer):
        cursor = self.conn.cursor()
        filterEntries = "SELECT id, description, payee, amount FROM receipt WHERE payer=?"
        arguments = (payer,)
        list = []

        cursor.execute(filterEntries, arguments)
        rows = cursor.fetchall()
        for row in rows:
            list.append((row[0], str(row[1]), str(row[2]), row[3]))

        filterEntries = "SELECT id, description, payer, amount FROM receipt WHERE payee=?"
        arguments = (payer, )
        cursor.execute(filterEntries, arguments)
        rows = cursor.fetchall()
        for row in rows:
            list.append((row[0], str(row[1]), str(row[2]), -1 * row[3]))

        sorted_list = sorted(list, key=lambda x: x[0])
        list_without_ids = (map((lambda x: (x[1], x[2], x[3])) , sorted_list))

        return list_without_ids


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
