from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib import admin
from .forms import reservationForm, reviewForm
from .models import BookingSystem, Reviews
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied

def message(request):
    return HttpResponse("Test")


def home(request):
    return render(request, 'allauth/account/index.html')


def menu(request):
    return render(request, 'allauth/account/menu.html')


def info(request):
    return render(request, 'allauth/account/info.html')

    return render(request, 'menu-main.html')


def menu_starters(request):
    return render(request, 'allauth/account/menu-starters.html')


def booking(request):
    return render(request, 'allauth/account/booking.html')


def menu_drinks(request):
    return render(request, 'allauth/account/menu-drinks.html')


@login_required
def MakeBooking(request):
    if request.method == 'POST':
        form = reservationForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user_id = request.user.id
            booking.save()
            messages.success(request, 'Booking successfully made!')
            return render(request, 'allauth/account/index.html')
    else:
        form = reservationForm()
    return render(request, 'allauth/account/make_booking.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index.html")
        else:
            messages.error(request, 'Unable to make booking')
    else:
        form = RegisterForm()

    return render(request, "allauth/account/register.html", {"form": form})


def login(request):
    return render(request, 'allauth/account/login.html')


@login_required
def view_bookings(request):
    bookings = BookingSystem.objects.filter(user=request.user)

    if request.method == 'POST' and 'delete' in request.POST:
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(BookingSystem, pk=booking_id)
        booking.delete()
        return redirect('view_bookings.html')

    return render(request, 'allauth/account/view_bookings.html', {'bookings': bookings})


def menu_desserts(request):
    return render(request, 'allauth/account/menu-desserts.html')


def menu_main(request):
    return render(request, 'allauth/account/menu-main.html')


def edit_booking(request, booking_id):
    booking = get_object_or_404(BookingSystem, id=booking_id)
    if request.method == 'POST':
        form = reservationForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Successfully Changed Your Reservation!')
            return redirect('view_bookings')
    else:
        form = reservationForm(instance=booking)

    return render(request, 'allauth/account/edit-booking.html',
                  {'form': form, 'booking': booking})

@login_required
def create_review(request):
    if request.method == 'POST':
        form = reviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('index.html')
    else:
        form = reviewForm()

    return render(request, 'allauth/account/create_review.html', {'form': form})

def reviews_list(request):
    reviews = Reviews.objects.all().order_by('-created_at')
    return render(request, 'allauth/account/reviews_list.html', {'reviews': reviews})
