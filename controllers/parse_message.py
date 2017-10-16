from controllers.acknowledge_handler import acknowledge_handler
from controllers.add_handler import add_handler
from controllers.debt_handler import debt_handler
from controllers.history_handler import history_handler
from controllers.loan_handler import loan_handler
from controllers.give_handler import give_handler
from controllers.retract_handler import retract_handler
from controllers.start_handler import start_handler
import telepot
import Database

db = Database.Database()
paybot = telepot.Bot("452146569:AAFd8H6aj0ifJIpVT_zfxlSad8WOBUSjU2c")


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

    try:
        if db.userExists(user_id):
            if command == "start":
                start_handler(user_id, arguments)
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
            else:
                paybot.sendMessage(user_id, "Invalid Command")
        else:
            if command == "start":
                start_handler(user_id, username, arguments)
            else:
                paybot.sendMessage(user_id, "Try /start")
                print("POTENTIAL SQL INJECTION THREAT FROM {}!".format(user_id))

    except Exception as e:
        message_admins(e, user_id, username, message)
        print(e)

def message_admins(exception, user_id, username, message):
    EXCEPTION_TRIGGERED_MESSAGE = "Dear admin of @paybobbot, an exception has been triggered by {}. The exception message is: {}. "
    EXCEPTION_CAUSING_MESSAGE = "The message which cause the exception was: {} ".format(message)
    STATUS_URL = "https://dashboard.heroku.com/apps/paybob/deploy/github"
    REDEPLOY_MESSAGE = "To check the status or re-deploy, visit: {}.".format(STATUS_URL)
    admin_ids = [229191458, 197340571]
    user = username + ": " + str(user_id)
    for id in admin_ids:
        paybot.sendMessage(id, EXCEPTION_TRIGGERED_MESSAGE.format(user, str(exception)) + EXCEPTION_CAUSING_MESSAGE + REDEPLOY_MESSAGE)
