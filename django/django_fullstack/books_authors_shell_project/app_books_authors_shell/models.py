

from django.db import models

class Book(models.Model) :
    title = models.CharField(max_length=225)
    desc = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model) :
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes= models.CharField(max_length=45,default="nooooootes")
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
