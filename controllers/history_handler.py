import telepot
import math
from controllers.Database import Database
from controllers.utilities import isReceiving, getAbsoluteAmount

USAGE_MESSAGE = "`/history x` to display previous transactions"
USAGE_EXAMPLE = "`/history 25` or `/history all`"


NO_ENTRIES_REQUESTED_MESSAGE = "0 entries request!"
NO_ENTIRES_AVAILABLE_MESSAGE = "There are no transactions recorded"

'''
    Returns a list of recent transactions in chronological order limited to numEntries
        String user_id:  s       
        Integer numEntries:     number of entries in the list
'''
def history_handler(user_id, args):
    # Initialisation of bot
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")

    # Check for non-null arguments
    if args is None:
        paybot.sendMessage(user_id, USAGE_MESSAGE)
        return
    elif args[0] != "all":
        numEntries = args[0]
        message = "Transaction History (past " + numEntries + " entries):"
    else:
        numEntries = args[0]        
        message = "Transaction History:"
    
    # Initialisation of database and handler variables
    db = Database()
    # db.addUser("sushinoya", 197340571)
    # db.addReceipt("sushinoya", "reginleiff", "idk what fk", "100")
    # db.addReceipt("reginleiff", "sushinoya", "who knows", "9001")
    counter = 1
    history = db.selfHistory(user_id)

    # If 0 entries requested
    if numEntries == 0:
        paybot.sendMessage(user_id, NO_ENTRIES_REQUESTED_MESSAGE)
        return
    
    # If no history
    if history is None:
        paybot.sendMessage(user_id, NO_ENTIRES_AVAILABLE_MESSAGE)
        return

    # If history exists
    numHistoryEntries = len(history)
    history = db.selfHistory(user_id)
    if numEntries != "all": 
        history = history[math.min(0, numHistoryEntries - numEntries), numHistoryEntries]
    for transaction in slicedHistory:
        (description, transactee, amount) = transaction
        absAmount = getAbsoluteAmount(amount)
        if isReceiving(amount):
            message += return_message(counter, transactee, absAmount, description)
        else:
            message += payment_message(counter, transactee, absAmount, description)
        counter += 1
    paybot.sendMessage(user_id, message)
    return

'''
    Creates a paying message for history handler
        Integer index:      index of the entry
        String transactee:  username of recepient of payment
        Double amount:      amount in transaction
        String reason:      reason for payment
'''
def payment_message(index, transactee, amount, reason):
    return "\n" + index + ". Paid " + transactee + " $" + amount + ". Reason: " + reason


'''
    Creates a return message for history handler
        Integer index:      index of the entry
        String transactee:  username of payer
        Double amount:      amount in transaction
        String reason:      reason for return
'''
def return_message(index, transactee, amount, reason):
    return "\n" + index + ". Receivied $" + amount + " from " + transactee + ". Reason: " + reason

    
