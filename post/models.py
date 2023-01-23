from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    Title= models.CharField(max_length=100)
    Description= models.CharField(max_length= 9999999)
    DateTime= models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self):
        title= self.Title
        return f'{title}'