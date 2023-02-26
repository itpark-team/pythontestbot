import telebot
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

def get_quote():
    bash_response = requests.get("http://bashorg.org/casual")
    soup = bs(bash_response.text, "html.parser")

    quote = soup.find("div", class_="q")
    result = str(quote.find_all("div")[-1])

    result = result.replace("<div>","")
    result = result.replace("</div>","")
    result = result.replace("<br/>","\n")

    return result

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
        response = get_quote()
        
    bot.send_message(chat_id, response)

    log(f"TO {chat_id} send {response}")


bot.polling(none_stop=True, interval=0)