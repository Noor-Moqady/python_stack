from django.db import models
from datetime import datetime
from time import gmtime, strftime
from django.utils import timezone
import re
import bcrypt

 
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last Name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']= 'Invalid Email Address'
        if User.objects.filter(email=postData['email']).exists():
            errors["email"] = "This email is already exists"

        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm']:
            errors['password']= 'Password not match'
       
        if postData['birthday'] !=''  and (datetime.strptime(postData['birthday'], "%Y-%m-%d")) >= (datetime.now()):
            errors["birthday"] = "Birthday should be in the past"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.TextField()
    birthday= models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if not postData['title']:
            errors["title"] = "Title is required"
        if len(postData['desc']) < 5:
            errors["desc"] = "Last Name should be at least 5 characters"
        return errors

class Book(models.Model) :
    title = models.CharField(max_length=225)
    desc = models.TextField(null = True)
    uploaded_by = models.ForeignKey(User, related_name ='books_uploded', on_delete = models.CASCADE)
    users_who_like= models.ManyToManyField(User, related_name='books_liked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
