import random
from urllib.request import urlretrieve
from compose.app import bot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
token = "1556928449:AAEMRVBeO2O1kWc59XZKUCA9TLAvf4yz9wU"


def is_cities(message):
    cities = open('cities.txt', encoding='utf-8').read().split('\n')

    for city in cities:
        if message.text == city:
            return True
    return False


@bot.message_handler(content_types=["photo"])
def recieve_message(msg):
    bot.send_message(msg.chat.id, "Спасибо запополнение нашего архива фотографий ")
    file_id = msg.photo[-1].file_id
    url = "https://api.telegram.org/file/bot" + token + "/" + bot.get_file(file_id).file_path
    urlretrieve(url, "C://Users/dsizo/PycharmProjects/bot_MSHP/qwe.png")


@bot.message_handler(commands=['start_cities'])
def start_game(msg):
    bot.send_message(msg.chat.id, "Урра! Игра началась! Называй город")
    bot.send_sticker(msg.chat.id, "CAACAgIAAxkBAAECFepgVw0bFlcEJQ0EmUFil1fPtOOGcgACXAkAAnlc4glUFIxMZTcstB4E")


@bot.message_handler(content_types=["text"], func=is_cities)
def answer_cities(msg):
    if msg.text[-1] == 'ь':
        symbol = msg.text[-2].upper()
    else:
        symbol = msg.text[-1].upper()
    cities = open('cities.txt', encoding='utf-8').read().split('\n')
    cities_in_symbol = [city for city in cities if city[0] == symbol]
    city = random.choice(cities_in_symbol)
    bot.send_message(msg.chat.id, city)


@bot.message_handler(content_types=["text"])
def answer_cities(msg):
    bot.send_message(msg.chat.id, "Введи существующий город")


