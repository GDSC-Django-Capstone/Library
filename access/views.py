from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book

# Create your views here.

def index(request):
    


    return render(request,"index.html")


def register(request):
    return HttpResponse("reg")

def login(request):
    return HttpResponse("log")