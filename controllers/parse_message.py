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

def parse_handler(user_id, message):
    '''
    Passes on the user request to the specific controller
    ARGUMENTS:
    message: string
    RETURN TYPE: void
    '''
    command = message.split(' ')[0][1:]
    arguments = message.split(' ')[1:] if len(message.split(' ')) > 1 else None
    if command == "acknowledge":
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
        telepot.sendMessage(user_id, "Invalid Command")
