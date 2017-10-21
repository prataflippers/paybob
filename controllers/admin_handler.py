import telepot
import Database
from utilities import isReceiving
import math

USAGE_MESSAGE = "`/admin <chatID> <message>`"

# Initialise database
db = Database.Database()


def admin_handler(admin_user_id, arguments):

    # Initialisation of bot
    paybot = telepot.Bot("452146569:AAG0SaDSKuvln4Qks1aj52BdA7P3-hvz9gM")
    admin_user = db.getUsername(admin_user_id)

    if arguments is None:
        paybot.sendMessage(admin_user_id, USAGE_MESSAGE)
    else:
        customer_id = arguments[0]
        message = arguments[1]

        for arg in arguments[2:]:
            message += " " + arg 

        print(customer_id)
        print(message)
        paybot.sendMessage(customer_id, message)
