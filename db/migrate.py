from db.setup import create_table

def migrate(self):
    connection = self.conn
    usersTable(connection)
    receiptsTable(connection)
    pendingTable(connection)
    totalsTable(connection)

def usersTable(connection):
    makeUserandIDtable = """CREATE TABLE IF NOT EXISTS user (
                            id Integer PRIMARY KEY AUTOINCREMENT,
                            username Text NOT NULL UNIQUE,
                            chatID Integer NOT NULL UNIQUE
                        );"""
    create_table(connection, makeUserandIDtable)

def receiptsTable(connection):
    makeReceipts = """CREATE TABLE IF NOT EXISTS receipt (
                        id Integer PRIMARY KEY AUTOINCREMENT,
                        payer Integer NOT NULL,
                        payee Integer NOT NULL,
                        description Text,
                        amount Float NOT NULL

                    );"""
    create_table(connection, makeReceipts)

def pendingTable(connection):
    makePending = """CREATE TABLE IF NOT EXISTS pending (
                        id Integer PRIMARY KEY AUTOINCREMENT,
                        payer Integer NOT NULL,
                        payee Integer NOT NULL,
                        description Text,
                        amount Float NOT NULL
                    );"""
    create_table(connection, makePending)

def totalsTable(connection):
    makeTotals = """CREATE TABLE IF NOT EXISTS total (
                            id Integer PRIMARY KEY AUTOINCREMENT,
                            payer Integer NOT NULL,
                            payee Integer NOT NULL,
                            amount Float NOT NULL
                );"""
    create_table(connection, makeTotals)
