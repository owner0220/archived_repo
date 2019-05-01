from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    audi = models.IntegerField()
    score = models.IntegerField()
    summary = models.CharField(max_length=200)
    poster_url = models.CharField(max_length=300)
    preview_url = models.CharField(max_length=300)