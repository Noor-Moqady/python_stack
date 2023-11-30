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
            if request.POST['birthday'] != '':
                user=User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'],password=pw_hash, birthday=request.POST['birthday'])
                request.session['logged_user_firstname']=user.first_name
                request.session['logged_user_id']=user.id
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user=User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'],password=pw_hash)
                request.session['logged_user_firstname']=user.first_name
                request.session['logged_user_id']=user.id
        return redirect('/success')
    


def welcome(request):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/')
    else:
        return render(request,"welcome.html")
    

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
                return redirect('/success')
            else:
                messages.error(request,"Invalid Password")
                return redirect('/')
        else:
            messages.error(request,"Invalid email address")
            return redirect('/')    

def logout(request):
    request.session.flush()
    return redirect('/')