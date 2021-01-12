from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name="main"),
    path('home', views.home, name="home"),
    path('tree', views.tree, name="tree"),
    path('cards', views.cards_index, name="cards_index")
]
