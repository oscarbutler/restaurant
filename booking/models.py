from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookingSystem(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=20)
    Email = models.EmailField()
    Date = models.DateField()
    Time = models.TimeField()
