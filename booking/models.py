from django.db import models
from django.contrib.auth.models import User
from django.views import generic
from datetime import time
from .constants import different_times, amount_of_people
import datetime

class BookingSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(choices=different_times)
    number_of_people = models.CharField(choices=amount_of_people)
    

