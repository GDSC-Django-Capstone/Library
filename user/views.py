from django.shortcuts import render,redirect
from django.http import HttpResponse
from book.models import Book
from user.models import User
from user.models import Tracker

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

            
            user = User.objects.get(pk=uid)

            if str(book_id) not in user.borrowed:
                return JsonResponse({'msg':"Check if you have successfully borrowed the book or try refreshing the page"})
            

            tracked = Tracker.objects.filter(uid=uid,bid=book_id)

            if tracked:
                return JsonResponse({'msg':"Your return request is already pending"})
                
            
            book = Book.objects.get(pk=book_id)

            new_tracker = Tracker(tracking="return",email=user.email,title=book.title,uid=user.id,bid=book_id)

            new_tracker.save()
            
            return JsonResponse({'msg':"Return request has been sent successfully"})

        
            
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})
