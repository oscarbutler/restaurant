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
    time = models.TimeField(choices=different_times)
    number_of_people = models.IntegerField(choices=amount_of_people)


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    review_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
