from django.shortcuts import render,get_object_or_404
from movies.models import Movie
from django.core.files import File
from django.conf import settings


media_dir = settings.MEDIA_ROOT


def top_rank(request):
    thisu = Movie.objects.all()
    with open(media_dir+'/recent_update.txt','w') as f:
        myfile = File(f)
        myfile.write('is this writing to text??')
    return render(request,"top_rank.html", {"thisu":thisu})