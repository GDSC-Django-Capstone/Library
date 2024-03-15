from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book
from user.models import User

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    try:
        
        if request.method == "GET":
            
                books = Book.objects.all().order_by("-id")[:15]

                request.session['bnum'] = len(books)

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
            return JsonResponse({'msg':"method not supported"})

    except:
            return JsonResponse({'msg':"Unexpected error, try reloading the page"})












@csrf_exempt
def register(request):
    try:
        if request.method == "GET":

            return render(request,"register.html")
        
        elif request.method == "POST":
            try:
                data = json.loads(request.body)

                new_user = User(email=data['email'],password=data['password'],fname=data['fname'],lname=data['lname'],role='user')
                new_user.save()

                request.session['uid'] = new_user.id
                request.session['role'] = new_user.role
                request.session['bnum'] = 0
                request.session['cnum'] = 0


                return JsonResponse({'msg':'User registered successfully','task':'redirect'})
            except Exception as e:
                return JsonResponse({'msg':str(e)})

        else:
            return JsonResponse({'msg':"method not supported"})

    except Exception as e:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})










@csrf_exempt
def login(request):
    try:
        if request.method == "GET":

            return render(request,"login.html")
        
        elif request.method == "POST":
            try:
                data = json.loads(request.body)

                user = User.objects.filter(email=data['email'])
                
                if (not user) or (data['password'] != user[0].password):
                    return JsonResponse({'msg':'Incorrect email or password'})
                

                logged_user=user[0]


                request.session['uid'] = logged_user.id
                request.session['role'] = logged_user.role
                request.session['bnum'] = 0
                request.session['cnum'] = 0


                return JsonResponse({'msg':'User logged in successfully','task':'redirect'})
            
            except Exception as e:
                return JsonResponse({'msg':str(e)})

        else:
            return JsonResponse({'msg':"method not supported"})

    except Exception as e:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})

