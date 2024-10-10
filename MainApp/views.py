from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item


def home(request):
    return render(request, 'index.html')


def about(request):
    context = {
        'name': 'Master',
        'middle_name': 'Podelkovich',
        'surname': 'Samodelkin',
        'tel_number': '8-007-111-22-33',
        'email': 'yasam@hop.com'
    }
    return render(request, 'about.html', context)


# items = [
#    {"id": 1, "name": "Кроссовки abibas", "quantity":5},
#    {"id": 2, "name": "Куртка кожаная", "quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
#    {"id": 7, "name": "Картофель фри", "quantity":0},
#    {"id": 8, "name": "Кепка", "quantity":124},
# ]


def get_item(request, number):
    items = Item.objects.all()
    for item in items:
        if item.id == number:
            context = {'item': item}
            return render(request, 'item_page.html', context)
    text = f'Товар с id={number} не найден!'
    return HttpResponse(text)
 

def get_list_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'items_list.html', context)


