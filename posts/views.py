from django.shortcuts import render,redirect, get_object_or_404
from .forms import PostForm
from .models import Hashtag, Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# from django.http import HttpResponse
# Create your views here.
def post_lists(request):
    return render(request,"posts/posts.html")

def post_detail(request,p_id):
    return render(request,"posts/post_detail.html")
    

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request,"posts/form.html",{'form':form})

@login_required    
def post_delete(request,p_id):
    if request.method=="POST":
        post = get_object_or_404(Post,pk=p_id)
        post.delete()
        return redirect("/")
    else:
        return HttpResponse("Wrong Access 잘못된 접근입니다.")
    
@login_required
def post_update(request,p_id):
    user = get_user_model()
    me = request.user
    post = get_object_or_404(Post,pk=p_id)
    if user==me:
        if request.method=="POST":
            form = PostForm(request.POST,request.FILES,instance=post)
            print("11111111")
            if form.is_valid():
                print("2222")
                obj = form.save(commit=False)
                obj.save()
                return redirect("/")
        else:
            form = PostForm(instance=post)
    return render(request,"posts/form.html",{"form":form})
