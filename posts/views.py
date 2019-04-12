from django.shortcuts import render,redirect
from .forms import Postform,ImageForm,CommentForm
from .models import Post,Comment,Like
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models.query import EmptyQuerySet

# Create your views here.
def list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    return render(request,"posts/list.html",{'posts':posts,'comment_form':comment_form})
    
@login_required    
def create(request):
    #1. get 방식으로 데이터를 입력할 form요청
    if request.method == "POST":
        post_form = Postform(request.POST)
        image_form = ImageForm(request.POST,request.FILES)
        
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
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
    
@login_required
def update(request,id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        if request.method == "POST":
            post_form = Postform(request.POST,instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect("posts:list")
        else:
            post_form = Postform(instance=post)
        return render(request,'posts/form.html',{'post_form':post_form})
    else:
        return redirect('posts:list')
    
@login_required 
def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("posts:list")

@login_required
@require_POST
def comment_create(request,post_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST,request.user,Post.objects.get(id=post_id))
        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.user = request.user
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            return redirect("posts:list")
    
@login_required 
def comment_delete(request,post_id):
    comment = Comment.objects.get(id=post_id)
    if comment.user == request.user:
        comment.delete()
    return redirect("posts:list")
    
@login_required
def like(request,post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('posts:list')
    
    # if isinstance(post.like_set.filter(user=user),EmptyQuerySet) == True:
    #     like = post.like_set.filter(user=user)
    #     print("!!!2222222222222")
    #     like.delete()
    # else:
    #     like = Like(user=user,post=post)
    #     like.save()
    