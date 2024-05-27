from django.shortcuts import render
from django.http import HttpResponse
from .models import BookingSystem
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class reservationForm(forms.ModelForm):
    class Meta:
        model = BookingSystem
        fields = ['name', 'phone_number', 'email', 'date', 'time', 'number_of_people', ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=different_times),
        }

class RegisterForm(UserCreationForm):
    email = models.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
