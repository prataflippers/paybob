import telepot
import Database
from utilities import isReceiving
import math

USAGE_MESSAGE = "`/admin <chatID> <message>`"

# Initialise database
db = Database.Database()

def admin_handler(admin_user_id, arguments):

    # Initialisation of bot
    paybot = telepot.Bot("452146569:AAH0sXMgA9rtZe7j83L6RqqLU0qbo0sY12w")
    admin_user = db.getUsername(admin_user_id)

    if arguments is None:
        paybot.sendMessage(admin_user_id, USAGE_MESSAGE)
    else:
        customer_id = arguments[0]
        message = arguments[1]

        for arg in arguments[2:]:
            message += " " + arg

        paybot.sendMessage(customer_id, message)
