from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

# Create your views here.
def movielist(request):
    mlist = Movie.objects.all()
   
    t1 = Movie.objects.all().order_by('-score')[:4][0]
    t2 = Movie.objects.all().order_by('-score')[:4][1]
    t3 = Movie.objects.all().order_by('-score')[:4][2]
    return render(request,"watchlist/mlist.html", {"mlist":mlist,"t1":t1,"t2":t2,"t3":t3})
    
    
def mdetail(request,id):
    m = Movie.objects.get(id=id)
    return render(request,"watchlist/mdetail.html",{"m":m})
    
def mnew(request):
    return render(request,"watchlist/mnew.html")
    
def create(request):
    title = request.POST.get("title")
    title_en = request.POST.get("title_en")
    audience = request.POST.get("audience")
    open_date = datetime.strptime(request.POST.get("open_date"),"%Y-%m-%d").date()
    genre = request.POST.get("genre")
    watch_grade = request.POST.get("watch_grade")
    score = request.POST.get("score")
    poster_url = request.POST.get("poster_url")
    description = request.POST.get("description")
    
    data = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre,watch_grade=watch_grade,score=score,poster_url=poster_url,description=description)
    data.save()
    id = Movie.objects.latest('id').id
    return redirect(f"/movies/{id}")
    
def update(request,id):
    m = Movie.objects.filter(id=id)
    movie = Movie.objects.get(id=id)
    if request.method=="POST":
        title = request.POST.get("title")
        title_en = request.POST.get("title_en")
        audience = request.POST.get("audience")
        open_date = datetime.strptime(request.POST.get("open_date"),"%Y-%m-%d").date()
        genre = request.POST.get("genre")
        watch_grade = request.POST.get("watch_grade")
        score = request.POST.get("score")
        poster_url = request.POST.get("poster_url")
        description = request.POST.get("description")
        m.update(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre,watch_grade=watch_grade,score=score,poster_url=poster_url,description=description)
        return redirect(f"/movies/{id}")
    else:
        return render(request,"watchlist/medit.html",{"movie":movie})
        
def delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("/movies/")