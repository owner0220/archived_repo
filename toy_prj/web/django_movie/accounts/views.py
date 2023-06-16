from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm
from .models import User
# Create your views here.
def account_list(request):
    return HttpResponse("<h1>여기는 어카운트 페이지</h1>")

@login_required
def user_detail(request,id):
    thisu = get_object_or_404(User,pk=id)
    return render(request,"accounts/user_detail.html",{"thisu":thisu})

def sign_up(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    return render(request,"accounts/form.html",{'form':form})


def sign_in(request):
    if request.method=="POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request,"accounts/form.html",{"form":form})
    
@login_required
def sign_out(request):
    logout(request)
    return redirect("/")
    
    
