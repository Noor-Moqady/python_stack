from django.db import models
from datetime import datetime
from time import gmtime, strftime
 
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network description should be at least 3 characters"
        if 'desc' in postData and len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters if provided"
        if Show.objects.filter(title=postData['title']).exists():
            errors["title"] = "A show with this title already exists"
        # if 'date' in postData and (datetime.strptime(postData['date'], '%Y-%M-%D %H:%M:%S')) >= (datetime.now()):
        #     errors["date"] = "Release Date should be in the past"
        
        return errors


class Show(models.Model):
    title = models.CharField(max_length=225)
    network = models.CharField(max_length=225)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

