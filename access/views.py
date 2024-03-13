from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()[:5]
    # print(str(books[0].image).split("/")[-1])


    #this is temporary, this will change after the add book form is completed
    for i in books:
        i.image = "book/"+(str(i.image).split("/")[-1])

    return render(request,"index.html", {'books':books})


def register(request):
    return HttpResponse("reg")

def login(request):
    return HttpResponse("log")