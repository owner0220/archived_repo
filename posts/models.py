from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Hashtag(models.Model):
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.content
    
    
class Post(models.Model):
    content = models.CharField(max_length=100)
    post_img = ProcessedImageField(
                upload_to='posts/images', #저장 위치
                processors=[ResizeToFill(600,600)], #크기지정
                format='JPEG',
                options={'quality':90},
                )
    post_geo = models.CharField(max_length=100)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    top = models.BooleanField()

    