from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('main', views.main, name="main"),

    # HOME & ABOUT & NAVIGATION FEATURES
    path('', views.home, name="home"),


    # TOPICS & CATEGORIES ALL ORGANIZED
    path('tree/', views.tree, name="tree"),
    

    # VOCABULARY CARD INDEX
    path('cards/', views.cards_index, name="cards_index"),
    path('cards/<int:object_id>', views.card_detail, name="card_detail"),
    path('cards/<int:object_id>/delete/', views.card_delete, name="card_delete"),
    path('cards/<int:object_id>/edit/', views.card_edit, name="card_edit"),

        # AWS ADD PHOTO
    path('cards/<int:object_id>/add_photo/', views.add_photo, name="add_photo"),

    # FEATURE INDEX
    path('features/', views.feature_index, name="features_index"),

    # DESIGN BOARD
    path('design-board/', views.design_board, name="design_board"),


]
