from django.shortcuts import render
from .models import Post

# Create your views here.
def info(request):
    teachers =Post.objects.filter(cate="선생님").first()
    
    students =Post.objects.filter(cate="학생")
    
    return render(request,"info/index.html",{"teachers":teachers,"students":students})
    
    
def read(request,stname):
    post = Post.objects.get(name=stname)
    return render(request, "info/read.html",{"post":post})