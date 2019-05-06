from django.shortcuts import render,get_object_or_404
from datetime import date
from movies.models import Movie
from django.core.files import File
from django.conf import settings

media_dir = settings.MEDIA_ROOT


def top_rank(request):
    thisu = Movie.objects.filter(release_date__startswith=date.today().year).order_by('-audi')[0:10:1]
    print(type(thisu))
    with open(media_dir+'/recent_update.txt','w') as f:
        myfile = File(f)
        myfile.write('is this writing to text??')
    return render(request,"top_rank.html", {"thisu":thisu})