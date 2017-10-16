from controllers.acknowledge_handler import acknowledge_handler
from controllers.add_handler import add_handler
from controllers.debt_handler import debt_handler
from controllers.history_handler import history_handler
from controllers.loan_handler import loan_handler
from controllers.give_handler import give_handler
from controllers.retract_handler import retract_handler
import telepot
import Database

db = Database.Database()

def parse_handler(user_id, username, message):
    '''
    Passes on the user request to the specific controller
    ARGUMENTS:
    message: string
    RETURN TYPE: void
    '''
    # Initialisation of bot
    paybot = telepot.Bot("452146569:AAFd8H6aj0ifJIpVT_zfxlSad8WOBUSjU2c")
    command = message.split(' ')[0][1:]
    arguments = message.split(' ')[1:] if len(message.split(' ')) > 1 else None

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
            print("POTENTIAL SQL INJECTION THREAT FROM {}!".format(user_id))
