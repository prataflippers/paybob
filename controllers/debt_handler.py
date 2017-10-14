import telepot
from controllers.Database import Database
USAGE_MESSAGE = "`/debt <user>` to display amount owed to user, `/debt` to show current debt to all"
USER_NOT_FOUND = "Either specified user does not exist or is currently not using the bot. Please request for him/her to add @paybob"

def debt_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
    db = Database()

    # Handle paying
    payer = db.getUsername(user_id)

    # Display all debt
    if (arguments == None):
        allLoaners = db.owesToList(payer)
        allLoans = "" if len(allLoaners) > 0 else "Clean slate!!!"
        for loaner in allLoaners:
            print ("Loaner: " + loaner)
            debtOwed = db.getTotalsEntryId(payer, loaner[0])
            allLoans += print_debt(payer, loaner, debtOwed)
        paybot.sendMessage(user_id, allLoans)
    elif (db.getChatID(payee) == None):
        paybot.sendMessage(user_id, USER_NOT_FOUND)
    else:
        payee = arguments[0]
        debtOwed = db.getTotalsEntryId(payer, payee)
        paybot.sendMessage(print_debt(payer, payee, debtOwed))

def print_debt(payer, payee, amount):
    return "%s owes %s %d\n" % (payer, payee, amount)
