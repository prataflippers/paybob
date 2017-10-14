import Database
import telepot

# Messages
USAGE_MESSAGE = "Usage: `/pay <user> <amount>` to pay specified user the stipulated amount"
USER_NOT_FOUND = "Either specified user does not exist or is currently not using the bot. Please request for him/her to add @paybob"

def pay_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
    db = Database.Database()

    # For testing
    print("Current user: " + db.getUsername(user_id))
    print("Other user: " + arguments[0])

    # Handle paying
    try:
        if (len(arguments) < 2):
            paybot.sendMessage(user_id, USAGE_MESSAGE)
        elif (db.getChatID(arguments[0]) == None):
            paybot.sendMessage(user_id, USER_NOT_FOUND)
        elif(float(arguments[1])):
            paybot.sendMessage("Successfully payed %s to %s" % (arguments[1], arguments[0]))
        else:
            paybot.sendMessage(user_id, USAGE_MESSAGE)
    except:
        paybot.sendMessage(user_id, USAGE_MESSAGE)
