from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book

from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    try:
        
        if request.method == "GET":
            
                books = Book.objects.all().order_by("-id")[:15]

                request.session['bnum'] = 15

                #this is temporary, this will change after the add book form is completed
                for i in books:
                    i.image = "book/"+(str(i.image).split("/")[-1])

                return render(request,"index.html", {'books':books})
            

        elif request.method == "POST":
            bnum = request.session.get("bnum",0)
            query = Book.objects.all().order_by("-id")
            buffer = 15


            if bnum+buffer > len(query):
                books = query[bnum:]
                bnum = -buffer
            
            else:
                books = query[bnum:bnum+buffer]

            request.session['bnum'] = bnum+buffer

            data = {'data':[]}

            for book in books:
                data['data'].append({
                    "id":book.id,
                    "title":book.title,
                    "author":book.author,
                    "genre":book.genre,
                    "rating":book.rating,
                    "image":"static/book/"+(str(book.image).split("/")[-1]),
                })

            return JsonResponse(data)

        else:
            return HttpResponse("method not supported")

    except:
            return HttpResponse("Unexpected Error")


def register(request):
    try:
        if request.method == "GET":
            return render(request,"register.html")
        elif request.method == "POST":
            pass
        else:
            return HttpResponse("method not supported")

    except:
        return HttpResponse("Unexpected Error")

def login(request):
    try:
        if request.method == "GET":
            return render(request,"login.html")
        elif request.method == "POST":
            pass
        else:
            return HttpResponse("method not supported")

    except:
        return HttpResponse("Unexpected Error")