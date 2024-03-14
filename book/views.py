from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book

# Create your views here.
from django.http import JsonResponse
import json
# from django.views.decorators.csrf import csrf_exempt
















def info(request):
    try:
        if request.method == "GET":

            return render(request,"register.html")
        
        elif request.method == "POST":
            try:
                data = json.loads(request.body)

            except Exception as e:
                return JsonResponse({'msg':str(e)})

        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})























def search(request):
    try:
        if request.method == "GET":

            return render(request,"register.html")
        
        elif request.method == "POST":
            try:
                data = json.loads(request.body)

            except Exception as e:
                return JsonResponse({'msg':str(e)})
                
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})





















def borrow(request):
    try:
        if request.method == "GET":

            return render(request,"register.html")
        
        elif request.method == "POST":
            try:
                data = json.loads(request.body)

            except Exception as e:
                return JsonResponse({'msg':str(e)})
                
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})






















def comment(request):
    try:
        if request.method == "GET":

            return render(request,"register.html")
        
        elif request.method == "POST":
            try:
                data = json.loads(request.body)

            except Exception as e:
                return JsonResponse({'msg':str(e)})
                
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})



















def rate(request):
    try:
        if request.method == "GET":

            return render(request,"register.html")
        
        elif request.method == "POST":
            try:
                data = json.loads(request.body)

            except Exception as e:
                return JsonResponse({'msg':str(e)})
                
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})