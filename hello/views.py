from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Sakina Rezaie")
# Create your views here.
