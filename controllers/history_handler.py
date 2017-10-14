from utilities import isReceiving, getAbsoluteAmount

USAGE_MESSAGE = "`/history` to display previous transactions"

'''
    Returns a list of recent transactions in chronological order limited to numEntries
        String user_id:         
        Integer numEntries:     number of entries in the list
'''
def history_handler(user_id, numEntries):
    message = "Transaction History (past " + numEntries + " entries"
    counter = 1
    '''
    history = allHistory(user_id) 
    slicedHistory = history[len(history) - numEntries, len(history)]
    for transaction in slicedHistory:
        (description, transactee, amount) = transaction
        absAmount = getAbsoluteAmount(amount)
        if isReceiving(amount):
            message += return_message(counter, transactee, absAmount, description)
        else:
            message += payment_message(counter, transactee, absAmount, description)
        counter += 1
    send_message(user_id, message)
    '''

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

    
