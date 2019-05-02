from django.shortcuts import render,redirect
from .forms import PostForm
# from django.http import HttpResponse
# Create your views here.
def post_lists(request):
    return render(request,"posts/posts.html")

def post_detail(request,m_id):
    return render(request,"posts/post_detail.html")
    
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        print("1111")
        #raise()
        if form.is_valid():
            print("2222")
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request,"posts/form.html",{'form':form})