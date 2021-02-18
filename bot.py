import telebot
from main import total
import time
from datetime import datetime

bot = telebot.TeleBot('1650933252:AAG521soe0h6-YUaxQecJKPlss2Wd3kZrl4')
while True:
    now = datetime.now()
    bot.send_message(959339948, f'Баланс на {str(now).split(".")[0]} составляет {total}сом')
    time.sleep(3600)
