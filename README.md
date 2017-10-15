# PayBob
<p align="center">
  <img src="https://user-images.githubusercontent.com/23443586/31586777-66de891a-b208-11e7-9ce8-5c3752c60014.png" width=650 height=250>
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v2.7%20%2F%20v3.6-blue.svg)
![Heroku](http://heroku-badge.herokuapp.com/?app=angularjs-crypto&style=flat&svg=1)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/Clairvoyant.svg)](https://github.com/prataflippers/paybob/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## User Guide

This is a Telegram Bot to enable easy money tracking between two users. Find it at [**t.me/paybob**](https://t.me/paybob).

## Developer Guide

### Dependencies
- **Python 3.6**
- **pip 9.0**
- **pip packages:**
  - telepot (12.3)
  - urllib3 (1.22)
  - requests (2.18.4)

### Application Commands

These are the commands that are usable with the PayBobBot

- `/add recepient_name amount:` Documents the debt of `amount` to `recipient_name`
- `/give recepient_name amount:` Documents the payment of `amount` to `recipient_name`
- `/history number_of_entries recipient:` Requests for the transaction history between `recipient` up to `number_of_entries`
- `/history all:` Requests for your entire transaction history
- `/loans recipient_name:` Request for your loan history with `recipient_name`
- `/loans:` Request for your entire loan history

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
