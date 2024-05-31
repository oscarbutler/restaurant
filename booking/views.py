from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib import admin
from .forms import reservationForm
from .models import BookingSystem
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

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

@login_required
def MakeBooking(request):
    if request.method == 'POST':
        form = reservationForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user_id = request.user.id 
            booking.save()
            return render(request, 'booking_success.html')
    else:
        form = reservationForm()
    return render(request, 'make_booking.html', {'form': form})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("index.html")
    else:
        form = RegisterForm()

        return render(response, "register.html", {"form":form})

def login(request):
    return render(request, 'login.html')

