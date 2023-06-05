import telebot
import requests
from . import templates
from .models import Task
from django.shortcuts import render

bot = telebot.TeleBot(token='') # here is your telegram token


def send(request):
    name = request.POST.get('name')

    admin_id = 123456789    # here is your telegram id
    message = f"ЗАЯВКА!!\n\nОт {name}"
    bot.send_message(chat_id=admin_id, text=message)    



if __name__ == '__main__':
    send(requests)
