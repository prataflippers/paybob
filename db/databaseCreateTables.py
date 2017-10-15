def usersTable(self):
    makeUserandIDtable = """CREATE TABLE IF NOT EXISTS user (
                            id Integer PRIMARY KEY AUTOINCREMENT,
                            username Text NOT NULL UNIQUE,
                            chatID Integer NOT NULL UNIQUE
                        );"""
    self.create_table(self.conn, makeUserandIDtable)


def receiptsTable(self):
    makeReceipts = """CREATE TABLE IF NOT EXISTS receipt (
                        id Integer PRIMARY KEY AUTOINCREMENT,
                        payer Integer NOT NULL,
                        payee Integer NOT NULL,
                        description Text,
                        amount Float NOT NULL

                    );"""
    self.create_table(self.conn, makeReceipts)

def pendingTable(self):
    makePending = """CREATE TABLE IF NOT EXISTS pending (
                        id Integer PRIMARY KEY AUTOINCREMENT,
                        payer Integer NOT NULL,
                        payee Integer NOT NULL,
                        description Text,
                        amount Float NOT NULL
                    );"""
    self.create_table(self.conn, makePending)

def totalsTable(self):
    makeTotals = """CREATE TABLE IF NOT EXISTS total (
                            id Integer PRIMARY KEY AUTOINCREMENT,
                            payer Integer NOT NULL,
                            payee Integer NOT NULL,
                            amount Float NOT NULL
                );"""
    self.create_table(self.conn, makeTotals)
