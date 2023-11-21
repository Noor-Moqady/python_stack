from django.shortcuts import render, HttpResponse, redirect
from.models import *


# FOR BOOK PAGES>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def handel_form(request):
    context= {
       'allbooks': Book.objects.all()
    }
    return render(request, "books_authors.html", context)

def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def specific_book(request, id):
    context={
        'specific_book':Book.objects.get(id=int(id)),
        'allauthors': Author.objects.all()
    }
    return render(request, "specific_book.html", context)

def addauthor_to_book(request,id2):
    specific_book=Book.objects.get(id=int(id2))
    specific_author=Author.objects.get(id=request.POST['authoselesct'])
    specific_book.authors.add(specific_author)
    return redirect('/books/'+str(id2))
    # return redirect(f'/books/{id2}')


# FOR AUTHOR PAGES>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def handel_authorform(request):
    context= {
       'allauthors': Author.objects.all()
    }
    return render(request, "authors.html", context)  

def add_author(request):
    Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], notes=request.POST['note'])
    return redirect('/authors')

def specific_author(request, id3):
    context={
        'specific_author': Author.objects.get(id=int(id3)),
        'allbooks': Book.objects.all()
    }
    return render(request, "specific_author.html", context)

def addbook_to_author(request, id4):
    specific_book=Book.objects.get(id=request.POST['bookselect'])
    specific_author=Author.objects.get(id=int(id4))
    specific_author.books.add(specific_book)
    return redirect('/authors/'+str(id4))