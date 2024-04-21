from django.shortcuts import render
from django.http import HttpResponse
from .models import BookingSystem
from django import forms

class reservationForm(forms.ModelForm):
    class Meta:
        model = BookingSystem
        fields = ['Name', 'Phone_number', 'Email', 'Date', 'Time', 'Number_Of_People', ]
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
        }