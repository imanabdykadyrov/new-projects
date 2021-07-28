import telebot
import os
from flask import Flask, request
import uuid
from image import image_to_bw

token = "1906796843:AAHkiZECJP7i13g_-vDGdx9bBjdfv4deoM4"

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Привет Жаным) Отправь мне любое фото")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
 bot.reply_to(message, message.text)


@bot.message_handler(content_types=['photo'])
def photo(message):
    save_url = "/Users/admin/new_project/image/"
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    image_name = str(uuid.uuid4())+'.jpg'
    downloaded_file = bot.download_file(file_info.file_path)
    with open(save_url + image_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    print(save_url + image_name)
    path_to_bw = image_to_bw(save_url + image_name)
    img = open(path_to_bw, 'rb')
    bot.send_photo(message.chat.id, img)
    os.remove(path_to_bw)


bot.polling()








