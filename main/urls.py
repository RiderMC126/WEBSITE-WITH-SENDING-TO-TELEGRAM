from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('zayavka', views.sign, name='zayavka'),
    path('send', views.send_email),
    path('test', views.test)


]
