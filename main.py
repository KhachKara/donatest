# https://core.telegram.org
# http://t.me/khach_donatest_bot

import telebot
from telebot.types import Message
from telebot import types
from envparse import Env
from telebot.types import Message
import json
import requests
from datetime import datetime


env = Env()
TOKEN = env.str('TOKEN')
ADMIN_CHAT_ID = env.int('ADMIN_CHAT_ID')
bot_link = env.str('bot_link')
bot_search_name = env.str('bot_search_name')


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('50 рублей')
    item2 = types.KeyboardButton('200 рублей')
    item3 = types.KeyboardButton('500 рублей')
    item4 = types.KeyboardButton('1000 рублей')
    markup.add(item1, item2, item3, item4)

    bot.send_message (message.chat.id, f'Привет {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text in ['50 рублей', '200 рублей']:
            bot.send_message(message.chat.id, 'Спасибо!')
        else:
            bot.send_message(message.chat.id, 'СуперСпасибо!')


bot.polling(none_stop=True)