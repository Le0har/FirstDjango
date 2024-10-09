from django.urls import path
from MainApp import views


urlpatterns = [
    path("", views.home),
    path("about", views.about),
    path("item/<int:number>", views.get_item),
    path("items", views.get_list_items),
    path("items/<int:number_li>", views.get_string_li),
]
