from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Очень важный текст о нас'
    }
    return render(request, 'main/about.html', context)


def contact_us(request):
    context = {
        'title': 'Home - Контакты',
        'content': 'Контактная информация',
        'text_on_page': '880005553535'
    }
    return render(request, 'main/contact_us.html', context)


def delivery_payment(request):
    context = {
        'title': 'Home - Доставка и оплата',
        'content': 'Доставка и оплата',
        'text_on_page': 'Доставка по всей России, оплата как угодно'
    }
    return render(request, 'main/delivery_payment.html', context)