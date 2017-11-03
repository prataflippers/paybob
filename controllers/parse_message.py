# Handlers
from acknowledge_handler import acknowledge_handler
from add_handler import add_handler
from debt_handler import debt_handler
from history_handler import history_handler
from loan_handler import loan_handler
from give_handler import give_handler
from retract_handler import retract_handler
from start_handler import start_handler
from admin_handler import admin_handler

# Messages
from messages import ACCESS_WITHOUT_START
from messages import EXCEPTION_TRIGGERED_MESSAGE
from messages import EXCEPTION_CAUSING_MESSAGE

# Modules 
import telepot
import Database
import Logger

logger = Logger.Logger()
db = Database.Database()
paybot = telepot.Bot("452146569:AAH0sXMgA9rtZe7j83L6RqqLU0qbo0sY12w")


def parse_handler(user_id, username, message):
    '''
    Passes on the user request to the specific controller
    ARGUMENTS:
    message: string
    RETURN TYPE: void
    '''
    # Initialisation of bot
    command = message.split(' ')[0][1:]
    arguments = message.split(' ')[1:] if len(message.split(' ')) > 1 else None

    # Logging
    logger.command_run(message, username, user_id)

    try:
        if db.userExists(user_id):
            if command == "start":
                start_handler(user_id, username, arguments)
            elif command == "acknowledge":
                acknowledge_handler(user_id, arguments)
            elif command == "add":
                add_handler(user_id, arguments)
            elif command == "debts":
                debt_handler(user_id, arguments)
            elif command == "history":
                history_handler(user_id, arguments)
            elif command == "loans":
                loan_handler(user_id, arguments)
            elif command == "give":
                give_handler(user_id, arguments)
            elif command == "retract":
                retract_handler(user_id, arguments)
            elif command == "admin":
                admin_handler(user_id, arguments)
            else:
                paybot.sendMessage(user_id, "Invalid Command")
        else:
            if command == "start":
                start_handler(user_id, username, arguments)
            else:
                paybot.sendMessage(user_id, "Try /start")
                print(ACCESS_WITHOUT_START.format(user_id))

    except Exception as e:
        message_admins(e, user_id, username, message)
        logger.warning(e)

def message_admins(exception, user_id, username, message):
    user = username + ": " + str(user_id)
    logger.notify_admins(EXCEPTION_TRIGGERED_MESSAGE.format(user, str(exception)) + EXCEPTION_CAUSING_MESSAGE)
