def parse_handler(message):
    '''
    Passes on the user request to the specific controller
    ARGUMENTS:
    message: string
    RETURN TYPE: void
    '''
    text = message["text"]
    command = text.split(' ')[0][1:]
    argument = text.split(' ', 1)[1] if len(text.split(' ', 1))>1 else None
    if command == "add":
        print("Add handler")
    elif command == "show":
        print("Show handler")
    elif command == "clear":
        print("Clear handler")
    else:
        print("Invalid command")
