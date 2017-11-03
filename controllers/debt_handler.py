# Messages
from messages import USER_NOT_FOUND

# Modules
import telepot
import Database

USAGE_MESSAGE = "`/debt <user>` to display amount owed to user, `/debt` to show current debt to all"

def debt_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAH0sXMgA9rtZe7j83L6RqqLU0qbo0sY12w")
    db = Database.Database()

    # Handle paying
    payer = db.getUsername(user_id)

    # Display all debt
    if (arguments == None):
        allLoaners = db.owesToList(payer)
        allLoans = "" if len(allLoaners) > 0 else "Clean slate!!!"
        for loaner in allLoaners:
            print ("Loaner: " + loaner[0])
            debtOwed = db.getTotalsEntryId(payer, loaner[0])
            allLoans += print_debt(payer, loaner, debtOwed)
        paybot.sendMessage(user_id, allLoans)
    elif (db.getChatID(arguments[0]) == None):
        paybot.sendMessage(user_id, USER_NOT_FOUND.format(arguments[0]))
    else:
        payee = arguments[0]
        debtOwed = db.getTotalsEntryId(payer, payee)
        paybot.sendMessage(print_debt(payer, payee, debtOwed))

def print_debt(payer, payee, amount):
    return "%s owes %s %d\n" % (payer, payee, amount)
