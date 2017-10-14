from utilities import isReceiving, getAbsoluteAmount
import telepot
import Database

USAGE_MESSAGE = "`/history` to display previous transactions"

'''
    Returns a list of recent transactions in chronological order limited to numEntries
        String user_id:         
        Integer numEntries:     number of entries in the list
'''
def history_handler(user_id, args):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
    db = Database.Database()

    # Initialise history handler variables
    numEntries = args[0]
    message = "Transaction History (past " + numEntries + " entries"
    counter = 1
    db = Database()

    history = db.selfHistory(user_id) 
    slicedHistory = history[len(history) - numEntries, len(history)]
    for transaction in slicedHistory:
        (description, transactee, amount) = transaction
        absAmount = getAbsoluteAmount(amount)
        if isReceiving(amount):
            message += return_message(counter, transactee, absAmount, description)
        else:
            message += payment_message(counter, transactee, absAmount, description)
        counter += 1
    paybot.send_message(user_id, message)

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

    
