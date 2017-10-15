import telepot
import Database
from utilities import isReceiving
import math

USAGE_MESSAGE = "`/loan <user>` to display loans to one user, `/loan` to display all"
NO_LOANS_MESSAGE = "You have not loaned anyone anything."

def loan_handler(user_id, arguments):
    # Initialisation of bot
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")

    # initialise database
    db = Database.Database()
    user = db.getUsername(user_id)

    if arguments is None:
        singleLoan = False
    else:
        singleLoan = True
        transactee = arguments[0]

    if singleLoan:
        amount = db.moneyOwed(user, transactee)
        paybot.sendMessage(user_id, single_loan_message(transactee, amount))
    else:
        loans = db.hasNotPaid(user)

        print(loans)
        db.printTable("user")
        if loans == None:
            paybot.sendMessage(user_id, NO_LOANS_MESSAGE)
        else:
            message = "Loans:"
            counter = 1
            for loan in loans:
                (transactee, amount) = loan
                message += "\n" + str(counter) + ". " + single_loan_message(username, amount)
                counter += 1
            paybot.sendMessage(user_id, message)
    return


def single_loan_message(transactee, amount):
    if isReceiving(amount):
        return transactee + " owes me $" + str(amount)
    else:
        absAmount = math.fabs(amount)
        return "I owe " + transactee + " $" + str(amount)
