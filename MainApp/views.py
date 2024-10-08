from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    text = """
    <h1>"Изучаем Django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)


def about(request):
    name = 'Ivan'
    middle_name = 'Petrovich'
    surname = 'Ivanov'
    tel_number = '8-923-745-33-22'
    email = 'ivan@hop.com'

    text = f"""
    <p>Имя: {name}</p>
    <p>Отчество: {middle_name}</p>
    <p>Фамилия: {surname}</p>
    <p>телефон: {tel_number}</p>
    <p>email: {email}</p>
    """
    return HttpResponse(text)


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def get_item(request, number):
    flag = False
    for i in items:
        if i['id'] == number:
            name = i['name']
            count = i['quantity']
            flag = True
    if flag == False:
        text = f'Товар с id={number} не найден!'
        return HttpResponse(text)
    text = f"""
    <p>Название: {name}</p>
    <p>Количество: {count}</p>
    """
    return HttpResponse(text)

def get_list_items(request):
    pass