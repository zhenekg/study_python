from django.shortcuts import render
from .models import *


menu = [
    {'title': "О", 'url_name': 'about'},
    {'title': "Шлюз", 'url_name': 'gate'},
    {'title': "АТС", 'url_name': 'ats'},
    {'title': "Логин", 'url_name': 'login'}
]


def home_page(request):
    posts = Hardware.objects.all()
    context_home_page = {
        'posts': posts,
        'menu': menu,
        'title': 'Сетка'
                         }
    return render(request, 'lanview/index.html', context=context_home_page)


def about_page(request):
    return render(request, 'lanview/about.html', {'menu': menu, 'title': "about"})


def ats_page(request):
    return render(request, 'lanview/about.html', {'menu': menu, 'title': "ats"})


def login_page(request):
    return render(request, 'lanview/about.html', {'menu': menu, 'title': "login"})


def gate_page(request):
    return render(request, 'lanview/about.html', {'menu': menu, 'title': "gate"})
