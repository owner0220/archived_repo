from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    cate = models.CharField(max_length=100)