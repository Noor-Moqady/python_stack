from django.shortcuts import render, HttpResponse, redirect
from.models import *

def handel_form(request):
    context = {
       'alldojos': Dojo.objects.all(),
       'allninjas':Ninja.objects.all()
    }
    return render(request, "dojo_ninja.html",context)
def add_dojo(request):
    Dojo.objects.create(name=request.POST['dojoname'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def add_ninja(request):
    Ninja.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], dojo=Dojo.objects.get(id=request.POST['dojoselesct']))
    return redirect('/')