from django.shortcuts import render
from django.http import HttpResponse
from .models import BookingSystem
from django import forms

class reservationForm(forms.ModelForm):
    class Meta:
        model = BookingSystem
        fields = ['name', 'phone_number', 'email', 'date', 'time', 'number_of_people', ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }