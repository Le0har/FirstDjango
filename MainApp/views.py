from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # text = """
    # <h1>"Изучаем Django"</h1>
    # <strong>Автор</strong>: <i>Иванов И.П.</i>
    # """
    # return HttpResponse(text)
    return render(request, 'index.html')


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
   {"id": 1, "name": "Кроссовки abibas", "quantity":5},
   {"id": 2, "name": "Куртка кожаная", "quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
   {"id": 7, "name": "Картофель фри", "quantity":0},
   {"id": 8, "name": "Кепка", "quantity":124},
]


def get_item(request, number):
    for item in items:
        if item['id'] == number:
            context = {'item': item}
        return render(request, 'item_page.html', context)
    text = f'Товар с id={number} не найден!'
    return HttpResponse(text)
 

def get_list_items(request):
    context = {'items': items}
    return render(request, 'items_list.html', context)


def get_string_li(request, number_li):
    text = f"""
    <p><a href="/items" style="text-decoration: none">&#8617; к списку товаров</a></p>
    <p>Название: {items[number_li - 1]['name']}</p>
    <p>Количество: {items[number_li - 1]['quantity']}</p>
    """
    return HttpResponse(text)