import time
import telepot
from telepot.loop import MessageLoop
import controllers.parse_message as parser

# Initial setup
paybot = telepot.Bot("452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ")
paybot.getUpdates(offset=100)

def handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        paybot.sendMessage(chat_id, msg['text'])
        parser.parse_handler(chat_id, msg['text'])

# Run loop
MessageLoop(paybot, handler).run_as_thread()

while 1:
    time.sleep(100)
