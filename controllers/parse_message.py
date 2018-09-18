# Messages
from messages import ACCESS_WITHOUT_START
from messages import EXCEPTION_TRIGGERED_MESSAGE
from messages import EXCEPTION_CAUSING_MESSAGE

# Modules
import telepot
import Logger

logger = Logger.Logger()
paybot = telepot.Bot("692962436:AAHOeT1VqRcAboPEBEaJjYKRfvJ9Mj9xCMw")


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
        if command == "time":
            paybot.sendMessage(user_id, getTime(), parse_mode= 'Markdown')  
        else:
            paybot.sendMessage(user_id, "Invalid Command")

    except Exception as e:
        message_admins(e, user_id, username, message)
        logger.warning(e)


def getTime(): 
    return "*Shitian*: {} \n*Haozhe*: {} \n*Suyash*: {}".format(timeInTimezone('Europe/Amsterdam'), timeInTimezone('Canada/Mountain'), timeInTimezone('Singapore'))

def timeInTimezone(timezone_name):
    from datetime import datetime
    from pytz import timezone

    zone = timezone(timezone_name)
    zone_time = datetime.now(zone)
    return zone_time.strftime('%H:%m hours on %d/%m/%Y')

def message_admins(exception, user_id, username, message):
    # user = username + ": " + str(user_id)
    # logger.notify_admins(EXCEPTION_TRIGGERED_MESSAGE.format(user, str(exception)) + EXCEPTION_CAUSING_MESSAGE)
