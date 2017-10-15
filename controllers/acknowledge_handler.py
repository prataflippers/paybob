import Database
import telepot
import yaml

# Messages
USAGE_MESSAGE = "Usage: `/acknowledge <user>` to acknowledge payment from user, `/acknowledge` to acknowledge all incoming payments"
USER_NOT_FOUND = "Either specified user does not exist or is currently not using the bot. Please request for him/her to add @paybob"
config = yaml.safe_load(open("../config.yml"))

def acknowledge_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot(config["telegram"]["TOKEN"])
    db = Database.Database()

    # Handle acknowledgement
    payer = arguments[0]
    payee = db.getUsername(user_id)
    amount = arguments[1]
    try:
        payee = db.getUsername(user_id)
        if (arguments == None):
            print(1)
            payer_id = None
            payeeMessage = ""
            allReceipts = db.getAllPending(payee)
            for receipt in allReceipts:
                payer = receipt[1]
                payee = receipt[2]
                description = receipt[3]
                amount = receipt[4]
                payer_id = db.getChatID(payer)
                db.incrementReceipt(payer, payee, description, amount)
                db.deleteAllPending(payee)
                paybot.sendMessage(payer_id, payer_message(amount, payee, description))
                payeeMessage += payee_message(amount, payer, description) + "\n"
            paybot.sendMessage(user_id, payeeMessage)
        else:
            payer = arguments[0]
            payer_id = db.getChatID(payer)
            if (db.getChatID(payee) == None):
                paybot.sendMessage(user_id, USER_NOT_FOUND)
            else:
                print(3)
                # Get pending receipt and create decrementReceipt
                receipt = db.getPending(payer, payee)[0]
                description = receipt[3]
                amount = receipt[4]
                db.incrementReceipt(payer, payee, description, amount)
                paybot.sendMessage(user_id, payee_message(amount, payee, description))
                paybot.sendMessage(payer_id, "Payment of ${} to {} acknowledged\nDescription: {}".format(amount, payer, payee))
    except Exception as e:
        print(5)
        paybot.sendMessage(user_id, USAGE_MESSAGE)
        print(e)

def payee_message(amount, payer, description):
    return "Successfully acknowledged payment of ${} from {}\nDescription: {}".format(amount, payer, description)

def payer_message(amount, payee, description):
    return "Payment of ${} to {} acknowledged".format(amount, payee, description)
