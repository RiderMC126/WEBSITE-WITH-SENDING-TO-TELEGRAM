from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
import smtplib
from django.core.mail import send_mail
import telebot

bot = telebot.TeleBot(token='6165128390:AAG1Rseq1CJOOZRqbWNf-bDduFwfS-QIPbY')


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def sign(requsts):
    return render(requsts, 'main/zayavka.html')

def test(request):
    return render(request, 'main/test.html')



def send_email(request):
    name = request.POST.get('name')
    post = request.POST.get('phone')
    admin_id = 123456789    # here is your telegram id

    message = f"ЗАЯВКА!!\n\nОт: {name}\n\nЦель: {post}"
    bot.send_message(chat_id=admin_id, text=message)

    return render(request, 'main/send.html')



 #    subject = 'Новая заявка!'
#    message = request.POST.get('name')
 #   email_from = 'mark.parshakov33@mail.ru'
 #   recipient_list = ['ridermc123@gmail.com', ]
 #   send_mail(subject, message, email_from, recipient_list)
  #  return HttpResponse("Successful")





