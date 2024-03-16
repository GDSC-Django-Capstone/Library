from django.shortcuts import render,redirect
from django.http import HttpResponse
from book.models import Book
from user.models import User

# Create your views here.
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def account(request):
    try:
        if request.method == "GET":

            uid = request.session.get("uid")
            role = request.session.get("role")

            if not uid or role != "user":
                return redirect("/login")
            

            user = User.objects.get(pk=uid)
            books = []

            for i in user.borrowed:
                books.append(Book.objects.get(pk=i))

            for i in books:
                i.image = "book/"+(str(i.image).split("/")[-1])

      

        
            return render(request,"account.html", {'fname':user.fname,'lname':user.lname,'email':user.email,'books':books})

        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})













    





@csrf_exempt
def return_book(request,book_id):
    try:
        if request.method == "POST":

            uid = request.session.get("uid")
            role = request.session.get("role")

            if not uid or role != "user":
                return JsonResponse({'msg':"Access Denied"})
            

                        
            return JsonResponse({'msg':"message"})

        
            
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})
