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


def get_item(request, number):
    try:
        one_item = Item.objects.get(id=number)
    except Item.DoesNotExist:
        text = f'Товар с id = {number} не найден!'
        return HttpResponse(text)
    else:
        context = {'item': one_item}
        return render(request, 'item_page.html', context)

def get_list_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'items_list.html', context)


