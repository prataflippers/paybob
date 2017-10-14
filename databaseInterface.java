--- DATABASE QUERY METHODS ---

void addUser(String username, int chatId);

void getChatID(String username);

void getUsername(int chatId);

//when payee says that someone owes him money
void makeReceipt(String payerUsername, String payeeUsername, int amount, String description);

//clears the receipts where the payer owed payee anything. i.e when the payer one shot pay everything
void paidEverything(String payerUsername, String payeeUsername, int amount);

//when the person who owed now owes more
void incrementReceipt(String payerUsername, String payeeUsername, int amount, String description);

//when the person who owed now owes more
void decrementReceipt(String payerUsername, String payeeUsername, int amount, String description);

//does payer owe payee anything
Boolean doesReceiptExist(String payerUsername, String payeeUsername);

//returns a list of all the people the 'username' owes money to and how much
[(Username, Amount)] owesMoneyTo(String username)

//returns a list of all the people that owe 'username' money and how much they owe
[(Username, Amount)] hasNotPaid(String username)

//returns a list of transactions between payer and payee.
//the amount is positive if payer paid and negative if payee paid
[(Description, Amount)] transactionHistory(String payerUsername, String payeeUsername);

//returns the amount user owes to a person
//if person owes money to user, amount will be negative
Amount moneyOwed (String username);

//returns a list of payments the user has made in the past
[(Description, Amount, paidTo)] payingHistory(String username);

//returns a list of payments the user has received in the past
[(Description, Amount, receivedFrom)] receivedHistory(String username);

//clears all transactions between user 1 and 2. They both owe each other 0 after this
void clearAllHistory(String username1, String username2);
