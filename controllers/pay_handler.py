import Database
import telepot

# Messages
USAGE_MESSAGE = "Usage: `/pay <user> <amount>` to pay specified user the stipulated amount"
USER_NOT_FOUND = "Either specified user does not exist or is currently not using the bot. Please request for him/her to add @paybob"

def pay_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
    db = Database.Database()

    # Handle paying
    try:
        payer = db.getUsername(user_id)
        payee = arguments[0]
        amount = arguments[1]
        payee_id = db.getChatID(payee)
        if (len(arguments) < 2):
            paybot.sendMessage(user_id, USAGE_MESSAGE)
        elif (db.getChatID(payee) == None):
            paybot.sendMessage(user_id, USER_NOT_FOUND)
        elif(float(amount) > 0):
            paybot.sendMessage(payee_id, "To acknowledge %s's payment of $%s, type `/acknowledge <user>`", (payer, amount))
            paybot.sendMessage(user_id, "Waiting for acknowledgement of payment of $%s to %s" % (amount, payee))
        else:
            paybot.sendMessage(user_id, USAGE_MESSAGE)
    except:
        paybot.sendMessage(user_id, USAGE_MESSAGE)
