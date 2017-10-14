import json
import requests
import urllib

TOKEN = "452146569:AAEdRQMubxBqRpSWYFs931wnUFja8vdHIIQ"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    '''
    ARGUMENTS:
    url: String
    RETURN TYPE: Response Object
    '''
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    '''
    ARGUMENTS:
    url: String
    RETURN TYPE: JSON Object
    '''
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    '''
    Long polling for updates
    ARGUMENTS:
    offset: Integer
    RETURN TYPE: JSON Object
    '''
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    '''
    ARGUMENTS:
    updates: Array<JSON>
    RETURN TYPE: Integer chat ID
    '''
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    '''
    Echoes all text messages within updates
    ARGUMENTS:
    updates: Array<JSON>
    RETURN TYPE: Void
    '''
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)


def get_last_chat_id_and_text(updates):
    '''
    Get last chat id and text
    ARGUMENTS:
    updates: Array<JSON>
    RETURN TYPE: Tuple(String text, Integer ID)
    '''
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    '''
    ARGUMENTS:
    text: String
    chat_id: Integer
    RETURN TYPE: Void
    '''
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def main():
    last_update_id = None
    while True:
        update = get_updates(last_update_id)
        if len(update["result"]) > 0:
            last_update_id = get_last_update_id(update) + 1
            echo_all(update)


if __name__ == '__main__':
    main()
