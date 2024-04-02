from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookingSystem(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = 
    Phone_number =
    Email =
    Data =
    Time =
    Number_of_people =