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
            

            tracked = Tracker.objects.filter(tracking="return",uid=uid,bid=book_id)

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























#Admin Views



@csrf_exempt
def add(request):
    try:

        zrole = request.session.get("role",0)

        if zrole == "admin" or zrole == "super":
            pass
        else:
            return JsonResponse({'msg':"Access Denied!"})

        if request.method == "GET":

            
            return render(request,"add.html")

        elif request.method == "POST":

            title = request.POST.get('title')
            author = request.POST.get('author')
            genre = request.POST.get('genre')
            amount = request.POST.get('amount')
            description = request.POST.get('description')
            image = request.FILES.get('image')


            new_book = Book(title=title,author=author,genre=genre,description=description,amount=amount,image=image)
            new_book.save()

            return JsonResponse({'msg':"Book added successfully","task":"erase"})
            
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})

























@csrf_exempt
def remove(request):
    try:
        zrole = request.session.get("role",0)

        if zrole == "admin" or zrole == "super":
            pass
        else:
            return JsonResponse({'msg':"Access Denied!"})

        if request.method == "GET":

            return render(request,"remove.html")

        elif request.method == "POST":

            data = json.loads(request.body)

            if data['task'] == "read":

                books = Book.objects.filter(title__icontains=data['title'])
                                
                if not books:
                    return JsonResponse({'msg':"Book not found!"})

                book = books[0]
                
                image = "static/book/"+(str(book.image).split("/")[-1])

                return JsonResponse({'status':"add","title":book.title,"author":book.author,"genre":book.genre,"rating":book.rating,"amount":book.amount,"image":image,"bid":book.id})

            elif data['task'] == "remove":
                
                book = Book.objects.get(pk=data['bid'])

                if not book:
                    return JsonResponse({'msg':"Book not found!"})

                if int(data['number']) > int(book.amount):
                    return JsonResponse({'msg':"Cant remove more than the available amount"})


                book.amount = int(book.amount) - int(data['number'])
                book.save()
                
                return JsonResponse({'msg':"Removed successfully"})

            else:
                return JsonResponse({'msg':"unsupported task"})

            
        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})































@csrf_exempt
def update(request):
    try:
        zrole = request.session.get("role",0)

        if zrole == "admin" or zrole == "super":
            pass
        else:
            return JsonResponse({'msg':"Access Denied!"})

        if request.method == "GET":
            
            return render(request,"update.html")
        
        elif request.method == "POST":

            data = json.loads(request.body)

            books = Book.objects.filter(title__icontains=data['title'])
                            
            if not books:
                return JsonResponse({'msg':"Book not found!"})

            book = books[0]
            
            image = "static/book/"+(str(book.image).split("/")[-1])

            return JsonResponse({'status':"add","title":book.title,"author":book.author,"genre":book.genre,"rating":book.rating,"amount":book.amount,"image":image,"bid":book.id})

        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})




























@csrf_exempt
def updater(request,book_id):
    try:
        zrole = request.session.get("role",0)

        if zrole == "admin" or zrole == "super":
            pass
        else:
            return JsonResponse({'msg':"Access Denied!"})

        if request.method == "GET":

            book = Book.objects.get(pk=book_id)

            if not book:
                return JsonResponse({'msg':"Book not found!"})

            
            return render(request,"updater.html", {'title':book.title,'author':book.author,'genre':book.genre,'amount':book.amount,'description':book.description,'bid':book.id})
        
        elif request.method == "POST":

            title = request.POST.get('title')
            author = request.POST.get('author')
            genre = request.POST.get('genre')
            amount = request.POST.get('amount')
            description = request.POST.get('description')
            image = request.FILES.get('image')


            book = Book.objects.get(pk=book_id)

            if not book:
                return JsonResponse({'msg':"Book not found!"})

            book.title = title
            book.author = author
            book.genre = genre
            book.amount = amount
            book.description = description

            if image:
                book.image = image


            book.save()
            

            return JsonResponse({'msg':"Book updated successfully","task":"redirect"})

        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})























@csrf_exempt
def returnBook(request):
    try:
        zrole = request.session.get("role",0)

        if zrole == "admin" or zrole == "super":
            pass
        else:
            return JsonResponse({'msg':"Access Denied!"})

        if request.method == "GET":

            tracked = Tracker.objects.filter(tracking="return").order_by('-id')[0:15]

            request.session['rnum'] = len(tracked)

            return render(request,"return.html", {'tracked':tracked})

        elif request.method == "POST":
            data = json.loads(request.body)

            if data['task'] == "load":

                rnum = request.session.get("rnum",0)
                query = Tracker.objects.filter(tracking="return").order_by('-id')
                buffer = 15


                if(int(rnum) >= len(query)):
                    return JsonResponse({'data':"end"})
                

                if rnum+buffer > len(query):
                    requests = query[rnum:]
                
                else:
                    requests = query[rnum:rnum+buffer]

                request.session['rnum'] = rnum+len(requests)

                data = {'data':[]}

                for i in requests:
                    data['data'].append({
                        'email':i.email,
                        'title':i.title,
                        'uid':i.uid,
                        'bid':i.bid,
                    })

                return JsonResponse(data)

            elif data['task'] == "return":
            

                uid = str(data['uid'])
                bid = str(data['bid'])


                if not uid or not bid:
                    return JsonResponse({'msg':"User or Book id not found!"})


                book = Book.objects.get(pk=bid)
                user = User.objects.get(pk=uid)

                if not book or not user:
                    return JsonResponse({'msg':"User or Book not found!"})


                book.amount = book.amount + 1

                user.borrowed.remove(bid)

                
                tracked = Tracker.objects.filter(uid=uid,bid=bid)

                book.save()
                user.save()

                for i in tracked:
                    i.delete()

                
                


                
                return JsonResponse({'task':"clear"})

            else:
                return JsonResponse({'msg':"unsupported task"})


        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})











@csrf_exempt
def lent(request):
    try:
        zrole = request.session.get("role",0)

        if zrole == "admin" or zrole == "super":
            pass
        else:
            return JsonResponse({'msg':"Access Denied!"})
            
        if request.method == "GET":

            tracked = Tracker.objects.filter(tracking="lent").order_by('-id')[0:15]

            request.session['lnum'] = len(tracked)

            return render(request,"lent.html", {'tracked':tracked})

        elif request.method == "POST":


            lnum = request.session.get("lnum",0)
            query = Tracker.objects.filter(tracking="lent").order_by('-id')
            buffer = 15


            if(int(lnum) >= len(query)):
                return JsonResponse({'data':"end"})
            

            if lnum+buffer > len(query):
                requests = query[lnum:]
            
            else:
                requests = query[lnum:lnum+buffer]

            request.session['lnum'] = lnum+len(requests)

            data = {'data':[]}

            for i in requests:
                data['data'].append({
                    'email':i.email,
                    'fname':i.fname,
                    'lname':i.lname,
                })

            return JsonResponse(data)



        else:
            return JsonResponse({'msg':"method not supported"})


    except:
        return JsonResponse({'msg':"Unexpected error, try reloading the page"})