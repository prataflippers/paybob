def addUser(self, username, chatId):
    addUser = "INSERT INTO user(username, chatID) VALUES (?, ?);"
    arguments = (username, chatId,)
    cursor = self.conn.cursor()
    cursor.execute(addUser, arguments)
    self.conn.commit()
    print("Added user {}: {} to the database".format(username, chatId))

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

def userExists(self, chatId):
    selectCommand = "SELECT id FROM user WHERE chatID=?"
    arguments = (chatId,)
    cursor = self.conn.cursor()
    cursor.execute(selectCommand, arguments)

    rows = cursor.fetchall()

    if rows != []:
        return True
    else:
        return False
