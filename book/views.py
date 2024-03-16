from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book
from user.models import User
from user.models import Tracker

# Create your views here.
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt















@csrf_exempt
def info(request,book_id):
    try:
        if request.method == "GET":

            book = Book.objects.get(pk=book_id)
            image = "book/"+(str(book.image).split("/")[-1])

            listed = book.reviews[0:30]
            reviews = []

            for i in range(int(len(listed)/2)):
                reviews.append([listed[i*2],listed[(i*2)+1]])

            request.session['cnum'] = len(listed)
            
            return render(request,"book.html", {'id':book.id,'title':book.title,'author':book.author,'genre':book.genre,'rating':book.rating,'amount':book.amount,'description':book.description,'image':image,'reviews':reviews})
        
        elif request.method == "POST":
            try:
                cnum = request.session.get("cnum",0)
                query = Book.objects.get(pk=book_id).reviews
                buffer = 30

                if(int(cnum) >= len(query)):
                    return JsonResponse({'data':"end"})
                

                if cnum+buffer > len(query):
                    comments = query[cnum:]
                
                else:
                    comments = query[cnum:cnum+buffer]

                request.session['cnum'] = cnum+len(comments)

                data = {'data':[]}

                for i in range(int(len(comments)/2)):
                    data['data'].append([comments[i*2],comments[(i*2)+1]])
                    

                return JsonResponse(data)






            except Exception as e:
                return JsonResponse({'msg':str(e)})

        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})






















@csrf_exempt
def search(request,book_name):
    try:
        if request.method == "GET":

            books = Book.objects.filter(title__icontains=book_name)

            for i in books:
                    i.image = "book/"+(str(i.image).split("/")[-1])


            return render(request,"search.html",{"name":book_name,"books":books})
        

        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})




















@csrf_exempt
def borrow(request,book_id):
    try:
        if request.method == "POST":
            try:
                uid = request.session.get("uid")

                if not uid:
                    return JsonResponse({'msg':"User not logged in","task":"redirect"})

                user = User.objects.get(pk=uid)
                book = Book.objects.get(pk=book_id)

                borrowed_list = user.borrowed
                number = len(borrowed_list)

                if number >= 3:
                    return JsonResponse({'msg':"You can only borrow a maximum of three books at a time"})

                if book_id in borrowed_list:
                    return JsonResponse({'msg':"You have already borrowed this book"})

                if book.amount <= 0:
                    return JsonResponse({'msg':"This book is currently unavailable"})
                    
                if user.banned:
                    return JsonResponse({'msg':"You are banned from borrowing books"})


                user.borrowed.append(book_id)
                user.history.append(book_id)
                user.history.append("0")
                book.amount = book.amount-1

                new_tracker = Tracker(tracking="lent",email=user.email,fname=user.fname,lname=user.lname,title=book.title)

                new_tracker.save()
                book.save()
                user.save()

                return JsonResponse({'msg':"Book successfully added to your borrowed list"})


            except Exception as e:
                return JsonResponse({'msg':str(e)})
                
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})





















@csrf_exempt
def comment(request,book_id):
    try:
        if request.method == "POST":
            try:
                data = json.loads(request.body)

                uid = request.session.get("uid")

                if not uid:
                    return JsonResponse({'msg':"User not logged in","task":"redirect"})

                user = User.objects.get(pk=uid)
                book = Book.objects.get(pk=book_id)
                
                history = user.history

                if book_id not in history:
                    return JsonResponse({'msg':"You can only comment on this book once you have borrowed it"})


                if data['comment'].replace(" ","") == "":
                    return JsonResponse({'msg':"Can't post empty comment"})

                
                name = user.fname + " " + user.lname

                
                book.reviews.insert(0,data['comment'])
                book.reviews.insert(0,name)

                book.save()

                


                return JsonResponse({'msg':"Comment was added successfully","task":"add", "name":name})

            except Exception as e:
                return JsonResponse({'msg':str(e)})
                
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})


















@csrf_exempt
def rate(request,book_id,rating):
    try:
        if request.method == "POST":
            try:
                uid = request.session.get("uid")

                if not uid:
                    return JsonResponse({'msg':"User not logged in","task":"redirect"})

                user = User.objects.get(pk=uid)
                book = Book.objects.get(pk=book_id)

                history = user.history

                
                if book_id not in history:
                    return JsonResponse({'msg':"You can only rate a book once you have borrowed it"})
                
                
                book_index = history.index(book_id)
                rate_index = book_index + 1

                
                if history[rate_index] != "0":
                    return JsonResponse({'msg':"You have already rated this book"})



                total_rates = int(book.total_rates)

                book.total_rates = total_rates + 1

                book.rating = ((int(book.rating) + int(rating)) / (total_rates + 1)) * 2


                book.save()

                history[rate_index] = rating
                user.save()




                return JsonResponse({'msg':"You have successfully rated this book"})
            except Exception as e:
                return JsonResponse({'msg':str(e)})
                
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})