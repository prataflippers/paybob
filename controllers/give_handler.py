# Messages
from messages import USER_NOT_FOUND
from messages import NEW_USER_ADD

# Modules
import Database
import telepot
import Logger

logger = Logger.Logger()
USAGE_MESSAGE = "Usage: `/give <user> <amount>` to pay specified user the stipulated amount"

def give_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAH0sXMgA9rtZe7j83L6RqqLU0qbo0sY12w")
    db = Database.Database()

    # Handle paying
    try:
        payee = arguments[0]
        amount = arguments[1]
        payer = db.getUsername(user_id)
        payee = arguments[0]
        amount = arguments[1]
        description = " ".join(arguments[2:])
        payee_id = db.getChatID(payee)
        if (len(arguments) < 2):
            paybot.sendMessage(user_id, USAGE_MESSAGE)
        elif (db.getChatID(payee) == None):
            paybot.sendMessage(user_id, USER_NOT_FOUND.format(payee))
            paybot.sendMessage(user_id, NEW_USER_ADD.format(payer))
        elif(float(amount) > 0):
            db.insertPending(payer, payee, description, amount)
            toAcknowledgeMessage = "To acknowledge {}'s payment of ${}, type `/acknowledge {} {} <description>`".format(payer, amount, payer, amount)
            paybot.sendMessage(payee_id, toAcknowledgeMessage)
            waitingForAcknowledgeMessage = "Waiting for acknowledgement of payment of ${} to {}".format(amount, payee)
            paybot.sendMessage(user_id, waitingForAcknowledgeMessage)
        else:
            paybot.sendMessage(user_id, USAGE_MESSAGE)
    except Exception as e:
        paybot.sendMessage(user_id, USAGE_MESSAGE)
        logger.notify_admins(e)
        logger.warning(e)
