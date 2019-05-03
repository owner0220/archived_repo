from django.shortcuts import render,get_object_or_404
from movies.models import Movie

def top_rank(request):
    thisu = Movie.objects.all()
    return render(request,"top_rank.html", {"thisu":thisu})