import telebot
import requests
from . import templates
from .models import Task
from django.shortcuts import render

bot = telebot.TeleBot(token='6165128390:AAG1Rseq1CJOOZRqbWNf-bDduFwfS-QIPbY')


def send(request):
    name = request.POST.get('name')

    admin_id = 502447701
    message = f"ЗАЯВКА!!\n\nОт {name}"
    bot.send_message(chat_id=admin_id, text=message)



if __name__ == '__main__':
    send(requests)