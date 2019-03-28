import json


def ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False,selective=False):
    return json.dumps({
        'keyboard': keyboard,
        'resize_keyboard': resize_keyboard,
        'one_time_keyboard': one_time_keyboard,
        'selective': selective
    })


def KeyboardButton(test, request_contact=False, request_location=False):
    return {
        'text': test,
        'request_contact': request_contact,
        'request_location': request_location
    }


def InlineKeyboardMarkup(inline_keyboard):
    return json.dumps({
        'inline_keyboard': inline_keyboard
    })

def InlineKeyboardButton(text, url=None, callback_data=None, switch_inline_query=None,
                         switch_inline_query_current_chat=None, callback_game=None, pay=None):
    return {
        'text': text,
        'url': url,
        'callback_data': callback_data,
        'switch_inline_query': switch_inline_query,
        'switch_inline_query_current_chat': switch_inline_query_current_chat,
        'callback_game': callback_game,
        'pay': pay
    }