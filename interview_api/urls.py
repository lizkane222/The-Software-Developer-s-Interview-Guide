from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('main', views.main, name="main"),

    # HOME & ABOUT & NAVIGATION FEATURES
    path('', views.home, name="home"),


    # TOPICS & CATEGORIES ALL ORGANIZED
    path('tree', views.tree, name="tree"),
    

    # VOCABULARY CARD INDEX
    path('cards/', views.cards_index, name="cards_index"),
    
    # FEATURE INDEX
    path('features/', views.feature_index, name="features_index")



]
