from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm
# Create your views here.
def account_list(request):
    return HttpResponse("<h1>여기는 어카운트 페이지</h1>")
    
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
    
def sign_out(request):
    logout(request)
    return redirect("/")