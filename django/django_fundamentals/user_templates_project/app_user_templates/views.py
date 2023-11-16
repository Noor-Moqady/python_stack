from django.shortcuts import render, redirect
from.models import User

def method1(request):
    return render(request, "user_templates.html")

def method2(request):
    User.objects.create(first_name =request.POST['firstname'], last_name =request.POST['lastname'], email_adress=request.POST['email'], age=request.POST['age'])
    return redirect ("/allusers")

def method3(request):
    context={
        "allusers": User.objects.all(),
    }
    return render(request, "user_templates.html" ,context)