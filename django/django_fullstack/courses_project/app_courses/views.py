from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from.models import *

def show_course(request):
    if request.method == 'GET':
        context={
        'allcourses': Course.objects.all(),
        'alldesc': Description.objects.all()
        }
        return render(request,"courses.html", context)
    if request.method == 'POST':
####################################################VALIDATION PART##########################################################
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            show=Course.objects.create(name=request.POST['name'],desc=Description.objects.create(content=request.POST['desc']))
        return redirect('/')

def course_specificone(request, id):
    context={
        'specific_course': Course.objects.get(id=id),
        'specific_desc': Description.objects.get(id=id)
        
    }
    return render(request,"specific_course.html", context)
def no(request):
    return redirect('/')
def delete(request, id):
    specific_course =Course.objects.get(id=id)
    specific_course.delete()
    return redirect('/')