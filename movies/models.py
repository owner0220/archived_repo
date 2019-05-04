from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    audi = models.IntegerField(blank=True,null=True)
    score = models.IntegerField(blank=True,null=True)
    summary = models.CharField(max_length=200,blank=True,null=True)
    poster_url = models.CharField(max_length=300,blank=True,null=True)
    preview_url = models.CharField(max_length=300,blank=True,null=True)