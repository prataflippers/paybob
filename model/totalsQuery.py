#Returns a list of all the people the 'username' owes money to and how much
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
    return list

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
    return list
