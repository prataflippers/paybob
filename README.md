# PayBob

## User Guide

This is a Telegram Bot to enable easy money tracking between two users. Find it at **t.me/paybob.**

## Developer Guide

### Dependencies
- **Python 3.6**
- **pip 9.0**
- **pip packages:**
  - telepot (12.3)
  - urllib3 (1.22)
  - requests (2.18.4)

### Database API
#### Initialise Database:
`db = Database()`

`db.setup()`

#### **Available Commands:**

- `setup():` Sets up the tables in the database

- `addUser(username, chatId):` Adds new user to the database

- `getChatID(username):` Returns the chatID of a user when it receives the username as argument

- `getUsername(chatId):` Returns the username of a user when it receives the chatID as argument

- `moneyOwed(payerUsername, payeeUsername):` Returns the amount user owes to a person. If person owes money to user, amount will be negative

- `addReceipt(payerUsername, payeeUsername, description, amount):` To be used when: 1. Payer pays back payee. 2. Payer lends payee money

- `payingHistory(username):` Returns a list of all the payments that the 'username' has made. Return type: [(paidTo, Description, Amount)]

- `receivingHistory(username):` Returns a list of all the payments that the 'username' has received. Return type: `[(receivedFrom, Description, Amount)]`

- `printTable(tableName):` Prints an entire database table row by row. Tables can be `user`, `receipt` or `total`

- `owesMoneyTo(username):` Returns a list of all the people the 'username' owes money to and how much. Return type: `[(Username, Amount)]`

- `hasNotPaid(username):` Returns a list of all the people that owe 'username' money and how much they owe. Return type: `[(Username, Amount)]`

- `incrementReceipt(payerUsername, payeeUsername, description, amount):` To be used when when the person who owed now owes more i.e. payer gives money to payee

- `decrementReceipt(payerUsername, payeeUsername, description, amount):` To be used when the person who owes now owes less i.e. payee returns some money

- `paidEverything(payerUsername, payeeUsername):` Clears all records between the payer and payee

- `transactionHistory(payerUsername, payeeUsername):` Returns a list of transactions between payer and payee. The amount is positive if payer paid and negative if payee paid. Return type: `[(Description, Amount)]`

#### NOTE: Please do not misuse the API-token which can be found at various parts of the code. It will be reset and abstracted away in a gitignored config file after the end of iNTUition 2017.
