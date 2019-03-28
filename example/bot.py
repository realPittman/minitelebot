from .minitelebot import Bot

bot = Bot('<TOKEN>')
methods = bot.Methods()


def main(update):
    chat_id = update['message']['chat']['id']
    text = update['message']['text']

    bot.sendMessage(chat_id=chat_id, text=text)

bot.run(main)
