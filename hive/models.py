from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    contact= models.CharField(max_length=20)
    message= models.CharField(max_length=200)