import Database
import telepot

# Messages
USAGE_MESSAGE = "Usage: `/acknowledge <user>` to acknowledge payment from user, `/acknowledge` to acknowledge all incoming payments"
USER_NOT_FOUND = "Either specified user does not exist or is currently not using the bot. Please request for him/her to add @paybob"

def acknowledge_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
    db = Database.Database()

    # Handle acknowledgement
    try:
        payee = db.getUsername(user_id)
        if (arguments == None):
            print(1)
            payer_id = None;
            payeeMessage = ""
            allReceipts = db.getAllPending(payee)
            for receipt in allReceipts:
                payer_id = db.getChatID(receipt[1])
                db.incrementReceipt(receipt[1], receipt[2], receipt[3], receipt[4])
                db.deleteAllPending(payee)
                paybot.sendMessage(payer_id, payer_message(receipt[4], receipt[2], receipt[2]))
                payeeMessage += payee_message(receipt[4], receipt[1], receipt[3]) + "\n"
            paybot.sendMessage(user_id, payeeMessage)
        else:
            payer = arguments[0]
            payer_id = db.getChatID(payer)
            if (db.getChatID(payee) == None):
                print(2)
                paybot.sendMessage(user_id, USER_NOT_FOUND)
            else:
                print(3)
                # Get pending receipt and create decrementReceipt
                receipt = db.getPending(payer, payee)[0]
                description = receipt[3]
                amount = receipt[4]
                db.incrementReceipt(receipt[1], receipt[2], receipt[3], receipt[4])
                paybot.sendMessage(user_id, payee_message(receipt[4], receipt[2], receipt[3]))
                paybot.sendMessage(payer_id, "Payment of ${} to {} acknowledged\nDescription: {}".format(receipt[4], receipt[1], receipt[2]))
    except Exception as e:
        print(5)
        paybot.sendMessage(user_id, USAGE_MESSAGE)
        print(e)

def payee_message(amount, payer, description):
    return "Successfully acknowledged payment of ${} from {}\nDescription: {}".format(amount, payer, description)

def payer_message(amount, payee, description):
    return "Payment of ${} to {} acknowledged".format(amount, payee, description)
