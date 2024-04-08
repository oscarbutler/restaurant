from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu.html', views.menu, name='menu'),
    path('info.html', views.info, name='info'),
    path('menu-drinks.html', views.menu_drinks, name='menu-drinks'),
    path('menu-starters.html', views.menu_starters, name='menu-starters'),
    path('menu-main.html', views.menu_main, name='menu-main'),
    path('menu-desserts.html', views.menu_desserts, name='menu-desserts'),
    path('index.html', views.home, name='home'),
]