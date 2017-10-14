import Database
import telepot

USAGE_MESSAGE = "Usage: `/add <user> <amount>` to add a someone who owes you $$$"
USER_NOT_FOUND = "Either specified user does not exist or is currently not using the bot. Please request for him/her to add @paybob"

def add_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
    db = Database.Database()

    # For testing
    print("Current user: " + db.getUsername(user_id))
    print("Other user: " + arguments[0])

    # Test if other user exists
    try:
        if (len(arguments) < 2):
            paybot.sendMessage(user_id, USAGE_MESSAGE)
        elif (db.getChatID(arguments[0]) == None):
            paybot.sendMessage(user_id, USER_NOT_FOUND)
        elif(float(arguments[1])):
            print("Execute add")
        else:
            paybot.sendMessage(user_id, USAGE_MESSAGE)
    except:
        paybot.sendMessage(user_id, USAGE_MESSAGE)
