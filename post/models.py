from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    Title= models.CharField(max_length=100)
    Description= models.CharField(max_length= 9999999)
    Name= models.CharField(default= None,max_length=100)
    DateTime= models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self):
        title= self.Title
        author= self.Name
        return f'{title}..[{author}]'