USAGE_MESSAGE = "`/acknowledge <user>` to acknowledge payment from user, `/acknowledge` to acknowledge all incoming payments"

def acknowledge_handler(user_id, other_user, amount):
    print("Acknowledge Handler")
