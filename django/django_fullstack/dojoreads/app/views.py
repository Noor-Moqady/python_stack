from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from.models import *


def registration_form(request):
    if request.method == 'GET':
        return render(request,"login_registration.html")
    if request.method == 'POST':
# VALIDATION PART############################################################################################################################################################################################################################################################
        errors = User.objects.basic_validator(request.POST)
        if request.POST['which_form'] == 'registration':
            request.session['registration']='registration'
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user=User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'],password=pw_hash)
                request.session['logged_user_firstname']=user.name
                request.session['logged_user_id']=user.id
        return redirect('/books')
    


def welcome(request):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/')
    else:
        latestBooks = Book.objects.all().order_by('-id')[:3]
        for i in range(len(latestBooks)):
            latestBooks[i].last_review = latestBooks[i].review_book.last()
        allbooks = Book.objects.all()
        for i in range(len(allbooks)):
            allbooks[i].first_review = allbooks[i].review_book.first()
        context = {
       'allbooks': allbooks,
       'latest3book': latestBooks
    }
        print(context['latest3book'][0].review_book.all())
    return render(request, "welcome.html",context)
    

def login(request):
    if request.method == 'GET':
        return render(request,"login_registration.html")
    
    if request.method == 'POST':
        if request.POST['which_form'] == 'login':
            request.session['login']='login'
        userlogged=User.objects.filter(email=request.POST['email'])
        if userlogged: 
            logged_user=userlogged[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_user_name']=logged_user.name
                request.session['logged_user_id']=logged_user.id
                return redirect('/books')
            else:
                messages.error(request,"Invalid Password")
                return redirect('/')
        else:
            messages.error(request,"Invalid email address")
            return redirect('/')  
  

def logout(request):
    request.session.flush()
    return redirect('/')

def addbook_review(request):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/')
    else:

        if request.method == 'GET':
                context={
            'allauthors':Author.objects.all()
        }
                return render(request,"addbook.html", context)
        if request.method == 'POST':
##### VALIDATION PART####################################################################################
            errors = Book.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/books/add')
##### VALIDATION PART####################################################################################  
            else:
                specific_author = {}
                if len(request.POST['author']) != 0:
                    specific_author=Author.objects.create(name=request.POST['author'])
                else:
                    specific_author=Author.objects.get(id = int(request.POST['authorselect']))
                specific_book=Book.objects.create(title=request.POST['title'],author=specific_author, uploded_by=User.objects.get(id=request.session['logged_user_id']))
                specific_review=Review.objects.create(book=specific_book,user=User.objects.get(id=request.session['logged_user_id']),review=request.POST['review'],rate=int(request.POST['rate']))
                return redirect('/books/'+str(specific_book.id))
    
def showbook(request, id):
    context={
        'specific_book':Book.objects.get(id=id)
    }
    return render(request,"specific_book.html", context)

def addreview(request, id):
    specific_review=Review.objects.create(book=Book.objects.get(id=id),user=User.objects.get(id=request.session['logged_user_id']),review=request.POST['review'],rate=int(request.POST['rate']))
    return redirect('/books/'+str(id))
def delete(request, id, id2):
    review=Review.objects.get(id=id)
    review.delete()
    return redirect('/books/'+str(id2))

def specific_user(request, id):
    context={
        'specific_user' : User.objects.get(id=id)
    }
    return render(request, "specific_user.html" , context)