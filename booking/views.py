from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin

# Create your views here.
def message(request):
    return HttpResponse("Test")

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def info(request):
    return render(request, 'info.html')

def menu_main(request):
    return render(request, 'menu-main.html')

def menu_starters(request):
    return render(request, 'menu-starters.html')

def menu_desserts(request):
    return render(request, 'menu-desserts.html')

def booking(request):
    return render(request, 'booking.html')

def menu_drinks(request):
    return render(request, 'menu-drinks.html')