import telebot
import random
from datetime import datetime

comp_number = -1
user_number = -1

def log(message):
    print(f"LOG {datetime.now()} --- {message}")

bot = telebot.TeleBot("5961916718:AAFkGnLVDwBh-iKKcUfVc9Jaz2wSPTpGV0Q")
log("BOT STARTED")

@bot.message_handler(content_types=["text"])
def start(user_message):
    global comp_number
    global user_number

    chat_id = user_message.chat.id
    request = user_message.text
    response = ""

    log(f"FROM {chat_id} received {request}")

    if request == '/start':
        comp_number = random.randint(1,100)
        response = "бот загадал число от 1 до 100, попробуйте отгадать это число"
    else:
        if request.isdecimal() == True:
            user_number = int(request)
            if user_number>comp_number:
                response = "введите поменьше"
            elif user_number<comp_number:
                response = "введите побольше"
            else:
                response = "вы угадали, введите /start для начала новой игры "
        else:
            response = "ошибка вы ввели не число"

    bot.send_message(chat_id, response)


    log(f"TO {chat_id} send {response}")


bot.polling(none_stop=True, interval=0)