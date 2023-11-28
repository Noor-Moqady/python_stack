from django.db import models
from datetime import datetime
from time import gmtime, strftime
 
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['name']) < 5:
            errors["name"] = "Name should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Description should be at least 15 characters"
        # if Course.objects.filter(name=postData['name']).exists():
        #     errors["title"] = "A course with this name already exists"
        return errors

class Description(models.Model):
    content = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=225)
    desc = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

