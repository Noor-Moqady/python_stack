from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt

def main(request):
    return render (request,'main.html')


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
            
    else:
        hash1= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        registered_user = User.objects.create(first=request.POST['fname'],alias=request.POST['alias'],email=request.POST['email'],password=hash1)
        messages.success(request, "Registered successfully")
        request.session['user_id']=registered_user.id
        request.session['user_name']=registered_user.first
        return redirect('/success')
def login(request):
    user = User.objects.filter(email=request.POST['lemail'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['lpassword'].encode(), logged_user.password.encode()):
            request.session['user_id']=logged_user.id
            request.session['user_name']=logged_user.first
            messages.success(request, "Login successfully")
            return redirect('/success')
        else:
            messages.error(request,'Invalid authentication')
            return redirect ('/')
    else:
        messages.error(request,'Invalid authentication')
        return redirect ('/')
    
def success(request):
    if 'user_id' in request.session:
        context={
            'username':request.session['user_name'],
            'allbooks':Book.objects.all(),
            'range':[1,2,3,4,5],
        }
        return render(request,'books_home.html',context)
    else:
        return redirect ('/')
def logout(request):
    request.session.flush()
    return redirect('/')

def addbook(request):
    context={
        'allauthours':Author.objects.all()
    }
    return render(request,'add_book.html',context)

def addbook_procces(request):
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.create(title=request.POST['title'],users = this_user)
    this_review = Review.objects.create(review_content = request.POST['add_review'],rating = request.POST['rate'],books = this_book,users = this_user)
    if len(request.POST['author_new']) > 0 :
        this_author = Author.objects.create(name=request.POST['author_new'])
    else:
        this_author = Author.objects.get(id=request.POST['author_select'])
    this_book.book_authors.add(this_author)
    return redirect ('/books/'+str(this_book.id))

def book_added(request,id):
    this_book=Book.objects.get(id=int(id))
    # this_book.authors=this_book.book_authors.all()
    context={
        'allbook':Book.objects.all(),
        'book':this_book,
        'range':[1,2,3,4,5],
    }
    return render(request,'book.html',context)

def addreview_procces(request):

    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=request.POST['book_id'])
    Review.objects.create(review_content = request.POST['add_review'],rating = request.POST['rating'], books = this_book, users = this_user)
    return redirect('/books/'+str(this_book.id))

def user(request,id):
    this_user=User.objects.get(id=int(id))
    counter=0
    for rev in this_user.reviews_user.all():
        counter+=1
    context={
        'user':this_user,
        'counter':counter
    }
    return render(request,'user.html',context)

def delete_book(request,id):
    this_book=Book.objects.get(id=int(id))
    this_book.delete()
    return redirect('/success')

def delete_review(request,id):
    this_review=Review.objects.get(id=int(id))
    this_book_id=this_review.books.id
    this_review.delete()
    return redirect('/books/'+str(this_book_id))