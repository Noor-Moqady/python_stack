from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from.models import *

def shows_table(request):
    context={
        'allshows': Show.objects.all()
    }
    return render(request,"shows.html", context)

def shows_form(request):
    if request.method == 'GET':
        return render(request,"new_show.html")
    if request.method == 'POST':
# VALIDATION PART############################################################################################################################################################################################################################################################
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            show=Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], desc=request.POST['desc'])
        return redirect('/shows/'+str(show.id))

def shows_specificone(request, id):
    context={
        'specific_show': Show.objects.get(id=id)
        
    }
    return render(request,"specific_show.html", context)

def shows_update(request, id):
    if request.method == 'GET':
        context={
        'specific_show': Show.objects.get(id=id)
    }
        return render(request,"edit_show.html", context)
    if request.method == 'POST':
# VALIDATION PART############################################################################################################################################################################################################################################################
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                show=Show.objects.get(id=id)
                messages.error(request, value)
            return redirect('/shows/' + str(show.id) + '/edit')
        else:
            show=Show.objects.get(id=id)
            show.title=request.POST['title']
            show.network=request.POST['network']
            show.release_date=request.POST['date']
            show.desc=request.POST['desc']
            show.save()
        return redirect('/shows/'+str(show.id))

def delete(request, id):
    specific_show=Show.objects.get(id=id)
    specific_show.delete()
    return redirect('/shows')