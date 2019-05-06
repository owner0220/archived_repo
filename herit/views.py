from django.shortcuts import render,get_object_or_404
from movies.models import Movie
from django.core.files import File
from django.conf import settings


media_root = settings.MEDIA_ROOT


# print(media_root)
def top_rank(request):
    thisu = Movie.objects.all()
    print("111111")
    with open(media_root+'\\test.txt','w') as f:
        myfile = File(f)
        myfile.write('\nis this writing to text??')
        print("22222")
    return render(request,"top_rank.html", {"thisu":thisu})