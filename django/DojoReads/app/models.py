from django.db import models
from datetime import datetime
from time import gmtime, strftime
from django.utils import timezone
import re
import bcrypt

 
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['name']) < 2:
            errors["name"] = "Name should be at least 2 characters"
        if len(postData['alias']) < 2:
            errors["alias"] = "Alias should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']= 'Invalid Email Address'
        if User.objects.filter(email=postData['email']).exists():
            errors["email"] = "This email is already exists"

        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm']:
            errors['password']= 'Password not match'
       
        return errors


class User(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model) :
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['title']) < 5:
            errors["title"] = "Description should be at least 5 characters"
        if Book.objects.filter(title=postData['title']).exists():
            errors["title"] = "This Title is already exists"
       
        return errors

class Book(models.Model) :
    title = models.CharField(max_length=225)
    author = models.ForeignKey(Author, related_name ='books_author', on_delete = models.CASCADE)
    uploded_by = models.ForeignKey(User, related_name ='books_uploded', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()    

class Review(models.Model) :
    book=models.ForeignKey(Book, related_name ='review_book', on_delete = models.CASCADE)
    user=models.ForeignKey(User, related_name ='review_user', on_delete = models.CASCADE)
    review = models.TextField(null = True)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)