import telebot
import random
from datetime import datetime


def log(message):
    print(f"LOG {datetime.now()} --- {message}")


bot = telebot.TeleBot("5961916718:AAFkGnLVDwBh-iKKcUfVc9Jaz2wSPTpGV0Q")
log("BOT STARTED")

@bot.message_handler(content_types=["text"])
def start(user_message):
    chat_id = user_message.chat.id
    request = user_message.text
    response = ""

    log(f"FROM {chat_id} received {request}")

    if request == '/start':
        response = "вы прислали команду старт"
    else:
        response = "неизвестная команда введите /start"

    bot.send_message(chat_id, response)

    log(f"TO {chat_id} send {response}")


bot.polling(none_stop=True, interval=0)

