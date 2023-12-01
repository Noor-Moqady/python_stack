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
            user=User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'],password=pw_hash)
            request.session['logged_user_firstname']=user.first_name
            request.session['logged_user_id']=user.id
            
            
        return redirect('/books')
    


def welcome(request):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/')
    else:
        context = {
       'allbooks': Book.objects.all(),
       'favorite_book': User.objects.get(id=request.session['logged_user_id']).books_liked.all()
    }
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
                request.session['logged_user_firstname']=logged_user.first_name
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


def addfavoritebooks(request):
    favbook=Book.objects.create(title=request.POST['title'], desc=request.POST['desc'],uploaded_by=User.objects.get(id=request.session['logged_user_id']))
    user_favbook=User.objects.get(id=request.session['logged_user_id'])
    user_favbook.books_liked.add(favbook)
    return redirect('/books')
def addfav(request, id):
    user_favbook=User.objects.get(id=request.session['logged_user_id'])
    favbook=Book.objects.get(id=int(id))
    user_favbook.books_liked.add(favbook)
    return redirect('/books')

def removefav(request, id):
    user_favbook=User.objects.get(id=request.session['logged_user_id'])
    favbook=Book.objects.get(id=int(id))
    user_favbook.books_liked.remove(favbook)
    return redirect('/books/'+str(id))

def update_specific_book(request, id):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/')
    else:

        if request.method == 'GET':
            context={
            'specific_book':Book.objects.get(id=int(id)),
            'logged_user':User.objects.get(id=int(request.session['logged_user_id']))
        }
            return render(request,"specific_book.html", context)
        if request.method == 'POST':
# ###########VALIDATION PART############################################################################################################################################################################################################################################################
            errors = Book.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    book=Book.objects.get(id=id)
                    messages.error(request, value)
                return redirect('/books/'+str(book.id))
            else:
                book=Book.objects.get(id=id)
                book.title=request.POST['title']
                book.desc=request.POST['desc']
                book.save()
            return redirect('/books/'+str(book.id))

def delete(request, id):
  specific_book=Book.objects.get(id=int(id))
  specific_book.delete()
  return redirect('/books')

