from django.urls import path
from . import views
from .views import MakeBooking, register, edit_booking
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
    path('view_bookings.html', views.view_bookings, name='view_bookings'),
    path('login/booking.html', views.booking, name="booking"),
    path('login/menu-drinks.html', views.menu_drinks, name='menu-drinks'),
    path('login/menu-main.html', views.menu_main, name='menu-main'),
    path('login/menu-starters.html', views.menu_starters,
         name='menu-starters'),
    path(
        'login/menu-desserts.html',
        views.menu_desserts,
        name='menu-drinks'
    ),
    path('login/index.html', views.home, name='home'),
    path('login/booking.html', views.booking, name='booking'),
    path('login/make_booking.html', views.MakeBooking, name='make-booking'),
    path('login/register.html', views.register, name='make-booking'),
    path('login.html', views.login, name='make-booking'),
    path('login/info.html', views.info),
    path('login/view_bookings.html', views.view_bookings,
         name='view_bookings'),
    path(
        'edit_booking/<int:booking_id>',
        views.edit_booking,
        name='edit_booking'
    ),
    path('make_booking', views.MakeBooking, name='make_booking'),
    path('reviews', views.create_review, name='create_review'),
    path('reviews_list.html', views.reviews_list, name='reviews_list'),
    path('login/reviews.html', views.create_review, name='create_review'),
    path('register/reviews.html', views.create_review, name='create_review'),
    path(
        'login/reviews_list.html',
        views.reviews_list,
        name='reviews_list'
    ),
    path(
        'register/reviews_list.html',
        views.reviews_list,
        name='reviews_list'
    ),
    path(
        'register/create_review.html',
        views.reviews_list,
        name='reviews_list'
    ),
    path(
        'login/create_review.html',
        views.create_review,
        name='reviews_list'
    ),
    path('reviews/', views.reviews_list, name='reviews_list'),
    path(
        'reviews/edit/<int:review_id>',
        views.edit_review,
        name='edit_review'
    ),
    path(
        'reviews/delete/<int:review_id>',
        views.delete_review,
        name='delete_review'
    ),
    path(
        'reviews/create_review.html',
        views.create_review,
        name='create_review'
    ),
    path('create_review.html', views.create_review, name='create_review'),
    path(
        'reviews/delete/index.html',
        views.delete_review,
        name='delete_review'
    ),
    path('reviews/delete/info.html', views.info, name='delete_review'),
    path(
        'reviews/delete/booking.hmtl',
        views.delete_review,
        name='delete_review'
    ),
    path(
        'reviews/delete/menu-starters.html',
        views.delete_review,
        name='delete_review'
    ),
    path(
        'reviews/delete/menu-main.html',
        views.delete_review,
        name='delete_review'
    ),
    path(
        'reviews/delete/menu-desserts.html',
        views.delete_review,
        name='delete_review'
    ),
    path(
        'reviews/index.html',
        views.home,
        name='reviews_list'
    ),
    path(
        'reviews/reviews_list.html',
        views.reviews_list,
        name='reviews_list'
    ),
    path(
        'reviews/menu-main.html',
        views.menu_main,
        name='reviews_list'
    ),
    path(
        'reviews/menu-desserts.html',
        views.menu_desserts,
        name='reviews_list'
    ),
    path(
        'reviews/info.html',
        views.info,
        name='reviews_list'
    ),
    path(
        'reviews/menu-starters.html',
        views.menu_starters,
        name='reviews_list'
    ),
    path(
        'reviews/menu-drinks.html',
        views.menu_drinks,
        name='reviews_list'
    ),
    path(
        'reviews/booking.html',
        views.booking,
        name='reviews_list'
    ),
    path(
        'reviews/make_booking.html',
        views.MakeBooking,
        name='reviews_list'
    ),
    path(
        'reviews/view_bookings.html',
        views.view_bookings,
        name='reviews_list'
    )
]
