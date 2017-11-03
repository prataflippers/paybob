import Database
import telepot
from messages import USER_NOT_FOUND
from messages import NEW_USER_ADD
from messages import INVALID_USERNAME
from utilities import isNumber
from utilities import isValidTelegramUsername

# Messages
USAGE_MESSAGE = "Usage: `/add <user> <amount>` to add a someone who owes you $$$"
# USER_NOT_FOUND = "@{} is currently not using the bot. Please request for him/her to add @paybobbot"
# NEW_USER_ADD = "@{} wants to connect with you on PayBob. Click on this link (t.me/paybobbot) to add PayBob to your telegram."
# INVALID_USERNAME = "The username entered is invalid"

def add_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAH0sXMgA9rtZe7j83L6RqqLU0qbo0sY12w")
    db = Database.Database()

    # Handle add
    try:
        assert (isValidArguments(arguments)),"Invalid Arguments"
        payer = db.getUsername(user_id)
        payee = arguments[0]
        amount = arguments[1]
        description = "Loaned {} ${}".format(payee, amount)
        if (len(arguments) == 3):
            description = arguments[2]

        if (not isValidTelegramUsername(payee)):
            paybot.sendMessage(user_id, INVALID_USERNAME)
        elif (db.getChatID(payee) == None):
            paybot.sendMessage(user_id, USER_NOT_FOUND.format(payee))
            paybot.sendMessage(user_id, NEW_USER_ADD.format(payer))
        elif(float(amount) > 0):
            paybot.sendMessage(user_id, "Successfully added receipt:\nLoaned ${} to {}".format(amount, payee))
            db.addReceipt(payer, payee, description, amount)
        else:
            paybot.sendMessage(user_id, USAGE_MESSAGE)

    except AssertionError:
        paybot.sendMessage(user_id, USAGE_MESSAGE)

def isValidArguments(args):
    return (args is not None) and (len(args) == 2 or len(args) == 3) and isNumber(args[1])
