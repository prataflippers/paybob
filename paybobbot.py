import time
import telepot

from telepot.loop import MessageLoop
from Database import Database
from controllers.parse_message import parse_handler

# Initial setup
paybot = telepot.Bot("452146569:AAH0sXMgA9rtZe7j83L6RqqLU0qbo0sY12w")
paybot.getUpdates(offset=100)

# Initialse Database
db = Database()
db.migrate()

def receiver(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        parse_handler(chat_id, msg["chat"]["username"], msg['text'])

# Run loop
MessageLoop(paybot, receiver).run_as_thread()

while 1:
    time.sleep(100)
