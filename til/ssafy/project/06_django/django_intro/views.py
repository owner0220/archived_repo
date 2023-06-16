from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Movie
# path('',views.mlist,name="list"),
# path('<id:int>',views.mdetail,name="detail"),
# path('<id:int>/delete',views.mdelete,name="delete"),
# path('<id:int>/update',views.mupdate,name="update"),

def mlist(request):
    posts = Movie.objects.all()
    return render(request,"movie/mlist.html",{'posts':posts})

def mdetail(request,id):
    post = Movie.objects.get(id=id)
    return render(request,"movie/mdetail.html",{'post':post})

def mdelete(request,id):
    post = Movie.objects.get(id=id)
    post.delete()
    return redirect("movies:list")

def mupdate(request,id):
    post = Movie.objects.get(id=id)
    if request.method=="POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    else:
        form = PostForm(instance=post)
    return render(request,"movie/form.html",{'form':form})