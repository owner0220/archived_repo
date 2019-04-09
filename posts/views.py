from django.shortcuts import render,redirect
from .forms import Postform,ImageForm
from .models import Post,Image

# Create your views here.
def list(request):
    posts = Post.objects.all()
    posts_img = Image.objects.all()
    return render(request,"posts/list.html",{'posts':posts,'posts_img':posts_img})
    
    
def create(request):
    #1. get 방식으로 데이터를 입력할 form요청
    if request.method == "POST":
        post_form = Postform(request.POST)
        image_form = ImageForm(request.POST,request.FILES)
        
        if post_form.is_valid():
            post = post_form.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form =ImageForm(request.POST,request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect("posts:list")
        else:
            pass
    else:
        #2. Postform을 인스턴스화 시켜서 form에 저장
        post_form = Postform()
        image_form = ImageForm()
    #3.form을 담아서 create.html을 보내준다.    
    return render(request,'posts/form.html',{'post_form':post_form,'image_form':image_form})
    
    
def update(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post_form = Postform(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("posts:list")
    else:
        post_form = Postform(instance=post)
        
    return render(request,'posts/form.html',{'post_form':post_form})
    
def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("posts:list")