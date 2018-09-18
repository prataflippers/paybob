import telepot

class Logger:

    def __init__(self):
        self.paybot = telepot.Bot("692962436:AAHOeT1VqRcAboPEBEaJjYKRfvJ9Mj9xCMw")


    def print_to_console(self, msg):
        print(msg)

    def notify_admins(self, msg):
        admin_ids = [197340571]
        for id in admin_ids:
            self.paybot.sendMessage(id, msg)

    def warning(self, msg):
        self.print_to_console("------------------WARNING----------------")
        self.print_to_console(msg)
        self.print_to_console("-----------------------------------------")

    def command_run(self, message, username, user_id):
        command = message.split(' ')[0][1:]
        arguments = message.split(' ')[1:] if len(message.split(' ')) > 1 else None
        self.print_to_console("------------------COMMAND----------------")
        self.print_to_console("User: {}: {}".format(username, user_id))
        self.print_to_console("Command Run: " + message)
        self.print_to_console("-----------------------------------------")
