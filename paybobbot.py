import time
import telepot

from telepot.loop import MessageLoop
from Database import Database
from controllers.parse_message import parse_handler

# Initial setup
paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
paybot.getUpdates(offset=100)

def handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    # Add user to database if s/he does not exist
    db = Database()
    db.setup
    if (db.getUsername(chat_id) == None):
        db.addUser(msg["chat"]["username"], chat_id)

    if content_type == 'text':
        parse_handler(chat_id, msg['text'])

# Run loop
MessageLoop(paybot, handler).run_as_thread()

while 1:
    time.sleep(100)
