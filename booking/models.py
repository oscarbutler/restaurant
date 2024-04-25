from django.db import models
from django.contrib.auth.models import User
from django.views import generic

class BookingSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
