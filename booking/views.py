from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin

# Create your views here.
def message(request):
    return HttpResponse("Test")

def home(request):
    return render(request, 'index.html')