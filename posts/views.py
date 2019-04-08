from django.shortcuts import render,redirect
from .forms import Postform
from .models import Post

# Create your views here.
def list(request):
    posts = Post.objects.all()
    
    return render(request,"posts/list.html",{'posts':posts})
    
    
def create(request):
    #1. get 방식으로 데이터를 입력할 form요청
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        else:
            pass
    else:
        #2. Postform을 인스턴스화 시켜서 form에 저장
        form = Postform()
    #3.form을 담아서 create.html을 보내준다.    
    return render(request,'posts/form.html',{'form':form})
    
    
def update(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = Postform(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = Postform(instance=post)
    return render(request,'posts/form.html',{'form':form})
    