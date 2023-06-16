from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .forms import MovieForm
from .models import Movie
from .api_update import *
import json

# Create your views here.
def movie_lists(request):
    movies = Movie.objects.all()
    return render(request,"movies/movie_list.html",{"movies":movies})
    
def movie_detail(request,id):
    movie = get_object_or_404(Movie,pk=id)
    return render(request,"movies/movie_detail.html",{"movie":movie})

@permission_required('movies.movie')
def movie_create(request):
    if request.method=="POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:movie_lists")
        
    else:
        form = MovieForm()
    return render(request,"movies/form.html",{"form":form})

@permission_required('movies.movie')
def movie_delete(request,id):
    if request.method=="POST":
        movie = get_object_or_404(Movie,pk=id)
        movie.delete()
        return redirect("/")
    else:
        return HttpResponse("Wrong Access 잘못된 접근입니다.")

@permission_required('movies.movie')        
def movie_update(request,id):
    if request.method=="POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        movie = get_object_or_404(Movie,pk=id)
        form = MovieForm(instance=movie)
        return render(request,"movies/form.html",{"form":form})

@permission_required('movies.movie')                
def movie_api_update(request,year):
    if past_year_update(year):
        return HttpResponse("Process is ~ing")
    else:
        return HttpResponse("Fail")