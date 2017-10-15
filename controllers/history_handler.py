import telepot
import math
import yaml

NO_ENTRIES_REQUESTED_MESSAGE = "0 entries request!"
NO_ENTIRES_AVAILABLE_MESSAGE = "There are no transactions recorded"
config = yaml.safe_load(open("../config.yml"))

'''
    Returns a list of recent transactions in chronological order limited to numEntries
        String user_id:         s
        Integer numEntries:     number of entries in the list
'''
def history_handler(user_id, args):
    # Initialisation of bot
    paybot = telepot.Bot(config["telegram"]["TOKEN"])
    # Check for non-null arguments
    if args is None:
        paybot.sendMessage(user_id, USAGE_MESSAGE)
        return
    elif args[0] != "all":
        numEntries = args[0]
        message = "Transaction History (past " + numEntries + " entries)"
    else:
        numEntries = args[0]
        message = "Transaction History"
    # Initialisation of database and handler variables
    db = Database.Database()
    counter = 1
    user = db.getUsername(user_id)
    # Individual or General transaction history
    if len(args) <= 1: # general history between transactee
        transactee = None
        history = db.history(user)
        message += ":"
    elif args[1] != "all": # individual history between transactee
        transactee = args[1]
        history = db.transactionHistory(user, transactee)
        message += " between " + transactee + ":"
    else:
        transactee = None
        history = db.history(user)
        message += ":"

    # If 0 entries requested
    if numEntries == 0:
        paybot.sendMessage(user_id, NO_ENTRIES_REQUESTED_MESSAGE)
        return
    # If no history
    if history is None:
        paybot.sendMessage(user_id, NO_ENTIRES_AVAILABLE_MESSAGE)
        return
    # If history exists
    numHistoryEntries = int(len(history))
    if numEntries != "all":
        numEntries = int(numEntries)
        start = max(0, numHistoryEntries - numEntries)
        history = history[start : numHistoryEntries]

    for transaction in history:
        if transactee == None:
            print(transaction)
            (description, transactor, amount) = transaction
            absAmount = math.fabs(amount)
            if isReceiving(amount):
                message += general_return_message(counter, transactor, absAmount, description)
            else:
                message += general_payment_message(counter, transactor, absAmount, description)
        else:
            (description, amount) = transaction
            absAmount = math.fabs(amount)
            if isReceiving(amount):
                message += individual_return_message(counter, transactee, absAmount, description)
            else:
                message += individual_payment_message(counter, transactee, absAmount, description)
        counter += 1
    paybot.sendMessage(user_id, message)
    return
'''
    Creates an individual paying message for history handler
        Integer index:      index of the entry
        String transactee:  username of recepient of payment
        Double amount:      amount in transaction
        String reason:      reason for payment
'''
def individual_payment_message(index, transactee, amount, reason):
    return "\n" + str(index) + ". Paid " + transactee + " $" + str(amount) + ". Reason: " + reason
'''
    Creates an individual return message for history handler
        Integer index:      index of the entry
        String transactee:  username of payer
        Double amount:      amount in transaction
        String reason:      reason for return
'''
def individual_return_message(index, transactee, amount, reason):
    return "\n" + str(index) + ". Received $" + str(amount) + " from " + transactee + ". Reason: " + reason
'''
    Creates an general paying message for history handler
        Integer index:      index of the entry
        String transactee:  username of recepient of payment
        Double amount:      amount in transaction
        String reason:      reason for payment
'''
def general_payment_message(index, transactee, amount, reason):
    return "\n" + str(index) + ". Paid $" + str(amount) + ". Reason: " + reason
'''
    Creates an general return message for history handler
        Integer index:      index of the entry
        String transactee:  username of payer
        Double amount:      amount in transaction
        String reason:      reason for return
'''
def general_return_message(index, transactee, amount, reason):
    return "\n" + str(index) + ". Received $" + str(amount) +". Reason: " + reason
