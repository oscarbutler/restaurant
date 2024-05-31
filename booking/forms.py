from django.shortcuts import render
from django.http import HttpResponse
from .models import BookingSystem
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Select
from .constants import different_times

class reservationForm(forms.ModelForm):
    class Meta:
        model = BookingSystem
        fields = ['name', 'phone_number', 'email', 'date', 'time', 'number_of_people', ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=different_times),
        }

    def TableLimit(self):

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
