from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("item/<int:number>", views.get_item, name='get-item'),
    path("items", views.get_list_items, name='get-list-items'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
