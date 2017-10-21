import Database
import telepot

# Messages
WELCOME_MESSAGE = "Welcome to PayBob!"
COMMANDS = """/add recepient_name amount: Documents the debt of amount to recipient_name
/give recepient_name amount: Documents the payment of amount to recipient_name
/history number_of_entries recipient: Requests for the transaction history between recipient up to number_of_entries
/history all: Requests for your entire transaction history
/loans recipient_name: Request for your loan history with recipient_name
/loans: Request for your entire loan history"""
WELCOME_BACK_MESSAGE = "Welcome Back to @paybobbot! We are constantly improving our services to help you better!"
ALREADY_STARTED_MESSAGE = "You are already using PayBob!"

def start_handler(user_id, username, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAH0sXMgA9rtZe7j83L6RqqLU0qbo0sY12w")
    db = Database.Database()

    if (arguments is None):
        if db.userExists(user_id):
            user = db.getUsername(user_id)
            paybot.sendMessage(user_id, WELCOME_BACK_MESSAGE)
        else:
            db.addUser(username, user_id)
            paybot.sendMessage(user_id, WELCOME_MESSAGE)
            paybot.sendMessage(user_id, COMMANDS)
    else:
        paybot.sendMessage(user_id, ALREADY_STARTED_MESSAGE)
