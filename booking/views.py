from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def message(request):
    return HttpResponse("Test")

def booking(request):