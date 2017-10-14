import Database
import telepot

# Messages
USAGE_MESSAGE = "Usage: `/acknowledge <user>` to acknowledge payment from user, `/acknowledge` to acknowledge all incoming payments"
USER_NOT_FOUND = "Either specified user does not exist or is currently not using the bot. Please request for him/her to add @paybob"

def acknowledge_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
    db = Database.Database()

    # Handle acknowledgement
    payee = arguments[0]
    amount = arguments[1]
    try:
        if (len(arguments) < 2):
            paybot.sendMessage(user_id, USAGE_MESSAGE)
        elif (db.getChatID(payee) == None):
            paybot.sendMessage(user_id, USER_NOT_FOUND)
        elif(float(amount)):
            payee_id = db.getChatID(payee)
            paybot.sendMessage(user_id, "Successfully acknowledged payment of %s from %s" % (amount, payee))
            paybot.sendMessage(payee_id, "Payment of %s to %s acknowledged", (db.getUsername(user_id), amount))
        else:
            paybot.sendMessage(user_id, USAGE_MESSAGE)
    except:
        paybot.sendMessage(user_id, USAGE_MESSAGE)
