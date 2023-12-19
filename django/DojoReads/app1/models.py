from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['fname']) < 2 :
            errors['name']= 'Name should be more than 5 characters'
        if len(postData['alias']) < 2 :
            errors['alias']= 'Alias should be more than 5 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']= 'Invalid Email Address'
        if postData['password'] != postData['confirm']:
            errors['password']= 'Password not match'
        return errors


class User(models.Model):
    first = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    password = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= UserManager()

class Author(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Book(models.Model):
    title = models.CharField(max_length=45)
    book_authors = models.ManyToManyField(Author, related_name="books")
    users = models.ForeignKey(User, related_name="books_user", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Review(models.Model):
    review_content = models.TextField()
    rating = models.IntegerField()
    books = models.ForeignKey(Book, related_name="reviews_book", on_delete = models.CASCADE)
    users = models.ForeignKey(User, related_name="reviews_user", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)