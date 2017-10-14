from Database import Database
USAGE_MESSAGE = "`/debt <user>` to display amount owed to user, `/debt` to show current debt to all"

db = Database()
token = "452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ"

def debt_handler(user_id, other_user, amount):
    bot = telepot.Bot(token)
    # amount = db.moneyOwed(other_user)
    if amount > 0:
      # send_message(user_id, "I owe this person $" + amount)
    elif amount < 0:
      # amount *= -1
      # send_message(user_id, "This person owes me $" + amount)
    else 
      # send_message(user_id, "No money owed here")
