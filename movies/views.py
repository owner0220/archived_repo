from django.shortcuts import render, redirect
from .forms import MovieForm,ScoreForm
from .models import *

# Create your views here.
def movie_page(request):
    movies = Movie.objects.all()
    return render(request,"movies/movie_page.html",{'movies':movies})
    
def movie_new(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            s = form.save()
    else:
        return render(request,"movies/form.html",{'form':form})
    return redirect("movies:movie_detail",s.id)
    
def movie_detail(request,movie_pk):
    movie = Movie.objects.get(id=movie_pk)
    return render(request,"movies/movie_detail.html",{'movie':movie})
    
    
def movie_edit(request,movie_pk):
    mv = Movie.objects.get(id=movie_pk)
    if request.method=="POST":
        form = MovieForm(request.POST,instance=mv)
        if form.is_valid():
            form.save()
    else:
        form = MovieForm(instance=mv)
        return render(request,"movies/form.html",{'form':form})
    return redirect("movies:movie_detail",movie_pk)
    
    
def scores_new(request,movie_pk):
    if request.method=="POST":
        form = ScoreForm(request.POST)
        movie = Movie.objects.get(id=movie_pk)
        if form.is_valid():
            score = form.save(commit=False)
            score.movie_id = movie
            form.save()
            print(type(form),type(score))
    else:
        form = ScoreForm()
        return render(request,"movies/form.html",{'form':form})
    return redirect("movies:movie_page")