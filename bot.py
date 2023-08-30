#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import os
from rembg import remove
from PIL import Image

API_TOKEN = '6251117170:AAFvlC1sEKA6VAXgG8ZTgjA782UXQsPInPw'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(content_types=['photo'])
def add_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    filename, file_ext = os.path.splitext(file_info.file_path)
    download_photo = bot.download_file(file_info.file_path)
    src = 'img/' +  message.photo[-1].file_id + file_ext
    
    with open(src, 'wb') as new_file:
        new_file.write(download_photo)
    
    create_photo(src)

    img = open("img/img_output.png", 'rb')
    bot.send_photo(message.chat.id, img)

    os.remove(src)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


def create_photo(src):
    input_patch = src
    output_patch = 'img/img_output.png'
    open_image = Image.open(input_patch)
    output = remove(open_image)
    output.save(output_patch)

bot.infinity_polling()

