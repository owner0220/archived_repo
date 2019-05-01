from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def post_lists(request):
    return render(request,"posts/posts.html")

def post_detail(request,m_id):
    return render(request,"posts/post_detail.html")
    
