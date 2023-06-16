from django.shortcuts import render,redirect
from .models import Genre,Score,Movie
from .forms import GenreForm,ScoreForm,MovieForm

# Create your views here.
def movies(request):
    movielist=Movie.objects.all()
    return render(request,"movies/movies.html",{'movielist':movielist})
    
def detail(request,id):
    moviedetail=Movie.objects.get(id=id)
    return render(request,"movies/detail.html",{'moviedetail':moviedetail})
    
    
def delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("movie:movies")

def update(request,id):
    m = Movie.objects.get(id=id)
    if request.method=="POST":
        m_form = MovieForm(request.POST,instance=m)
        if m_form.is_valid():
            m_form.save()
        return redirect("movie:movies")
    else:
        m_form = MovieForm(instance=m)
    return render(request,"movies/form.html",{"m_form":m_form})


def score_delete(request,id,sid):
    scor = Score.objects.get(id=sid)
    scor.delete()
    return redirect('movie:detail',id=scor.movie_id.id)

def score_new(request,id):
    m_form = ScoreForm()
    if request.method=="POST":
        score_form=ScoreForm(request.POST)
        if score_form.is_valid():
            form = score_form.save(commit=False)
            form.movie_id = Movie.objects.get(id=id)
            form.save()
            return redirect('movie:detail', id)
    return render(request,"movies/form.html",{"m_form":m_form})
    
def score_update(request,id,sid):
    data = Score.objects.get(id=sid)
    m_form = ScoreForm(instance=data)
    if request.method=="POST":
        score_form=ScoreForm(request.POST)
        if score_form.is_valid():
            form = score_form.save(commit=False)
            form.id = sid
            form.movie_id = Movie.objects.get(id=id)
            form.save()
            return redirect('movie:detail',id)
    return render(request,"movies/form.html",{"m_form":m_form})
   
   