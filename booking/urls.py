from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('info', views.info, name='info'),
    path('drinks', views.menu_drinks, name='menu-drinks'),
    path('starters', views.menu_starters, name='menu-starters'),
    path('mains', views.menu_main, name='menu-main'),
    path('desserts', views.menu_desserts, name='menu-desserts'),
]