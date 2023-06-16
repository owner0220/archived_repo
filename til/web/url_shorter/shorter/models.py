from django.db import models

# Create your models here.
class urlplace(models.Model):
    url = models.TextField()
    shorturl = models.TextField()
    custom = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.url