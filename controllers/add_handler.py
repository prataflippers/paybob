import Database
import telepot

USAGE_MESSAGE = "`/add <user> <amount>` to add a someone who owes you $$$"

def add_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
    db = Database.Database()

    # print("Current user: " + db.getUsername(user_id))
    # print("Other user: " + arguments[0])
