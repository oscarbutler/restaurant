from django.shortcuts import render
from django.http import HttpResponse

class reservation():
    class meta:
        fields = ['Name', 'Email', 'Phone_Number','Email','Date','Time','Number_Of_People']