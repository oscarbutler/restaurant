from django.shortcuts import render
from django.http import HttpResponse
from .models import BookingSystem, Reviews
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Select
from .constants import different_times
from datetime import date


class reservationForm(forms.ModelForm):
    class Meta:
        model = BookingSystem
        fields = ['name', 'phone_number', 'email',
                  'date', 'time', 'number_of_people']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=different_times),
        }

    def clean_date(self):
        booking_clean_date = self.cleaned_data.get('date')
        if booking_clean_date and booking_clean_date < date.today():
            raise forms.ValidationError("""You cant make a booking for a
            past date.""")
        return booking_clean_date

    def TableLimit(self):
        tables = super().clean()
        date = tables.get('date')
        time = tables.get('time')

        if date and time:
            AmountOfBookings = BookingSystem.objects.filter(date=date, time=time).count()
            if AmountOfBookings >= 10:
                raise forms.ValidationError("""There are no available tables
                for this time slot. Please choose a different time.""")

        return tables

    def clean(self):
        reservation_data = super().clean()
        date = reservation_data.get('date')
        time = reservation_data.get('time')

        max_reservations = 10

        if date and time:
            reservations = BookingSystem.objects.filter(date=date, time=time).count()
            if reservations >= max_reservations:
                raise forms.ValidationError("""There are no available
                reservations for this time slot. Please choose a different
                date or time.""")

        return reservation_data


class RegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.user_id = user.username
        if commit:
            user.save()
        return user


class reviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'review_comment']
        widgets = {
            'review_comment': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }
