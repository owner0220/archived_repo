from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    
class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    
    
class Score(models.Model):
    content = models.CharField(max_length=100)
    val = models.IntegerField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)