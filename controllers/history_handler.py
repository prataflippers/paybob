import telepot
import Database
from utilities import isReceiving, isPaying, getAbsoluteAmount

USAGE_MESSAGE = "/history \"x\" \"y\" to display x previous transactions between y (\"username\" or \"all\")"
USAGE_EXAMPLE = "/history 25 or /history all or /history 25 alberto or /history all alberto"


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
        message = "Transaction History (past " + numEntries + " entries)"
    else:
        numEntries = args[0]
        message = "Transaction History"

    # Initialisation of database and handler variables
    db = Database.Database()
    counter = 1
    user = db.getUsername(user_id)
    transactee = args[1]

    # Individual or General transaction history
    if transactee is None: # general history between transactee
        history = db.history(user)
        message += ":"
    else: # individual history between transactee
        history = db.transactionHistory(user, transactee)
        message += " between " + transactee + ":"

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
        (description, transactee, amount) = transaction
        absAmount = math.fabs(amount)
        # general receive
        if isReceiving(amount) and transactee == none:
            message += general_return_message(counter, transactee, absAmount, description)
        # individual receive
        elif isReceiving(amount) and transactee != none:
            message += individual_return_message(counter, transactee, absAmount, description)
        # general paying
        elif isPaying(amount) and transactee == none:
            message += general_payment_message(counter, transactee, absAmount, description)
        # individual paying
        else:
            message += general_payment_message(counter, transactee, absAmount, description)
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
    return "\n" + str(index) + ". Receivied $" + str(amount) + " from " + transactee + ". Reason: " + reason

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
    return "\n" + str(index) + ". Receivied $" + str(amount) +". Reason: " + reason
