from django.urls import path
from . import views
from .views import MakeBooking
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu.html', views.menu, name='menu'),
    path('info.html', views.info, name='info'),
    path('menu-drinks.html', views.menu_drinks, name='menu-drinks'),
    path('menu-starters.html', views.menu_starters, name='menu-starters'),
    path('menu-main.html', views.menu_main, name='menu-main'),
    path('menu-desserts.html', views.menu_desserts, name='menu-desserts'),
    path('index.html', views.home, name='home'),
    path('booking.html', views.booking, name='booking'),
    path('make_booking.html', views.MakeBooking, name='make-booking'),
    path('register.html', views.register, name="register"),
    # path('register/menu-drinks.html', views.menu_drinks, name='menu-drinks'),
    # path('register/menu-main.html', views.menu_main, name='menu-main'),
    # path('register/menu-starters.html', views.menu_starters, name='menu-starters'),
    # path('register/menu-desserts.html', views.menu_desserts, name='menu-drinks'),
    # path('register/index.html', views.home, name='home'),
    # path('register/booking.html', views.booking, name='booking'),
    # path('register/make_booking.html', views.MakeBooking, name='make-booking'),
    # path('register/menu-drinks.html', views.menu_drinks, name='menu'),
    path('view_bookings.html', views.view_bookings, name='view-bookings'),
    # path('login/booking.html', views.booking, name="booking"),
    # path('login/menu-drinks.html', views.menu_drinks, name='menu-drinks'),
    # path('login/menu-main.html', views.menu_main, name='menu-main'),
    # path('login/menu-starters.html', views.menu_starters, name='menu-starters'),
    # path('login/menu-desserts.html', views.menu_desserts, name='menu-drinks'),
    # path('login/index.html', views.home, name='home'),
    # path('login/booking.html', views.booking, name='booking'),
    # path('login/make_booking.html', views.MakeBooking, name='make-booking'),
    # path('login/register.html', views.register, name='make-booking'),
    path('login.html', views.login, name='make-booking'),
    # path('login/info.html', views.info,)
]