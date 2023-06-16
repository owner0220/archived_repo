from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def stlist(request):
    stlist = Student.objects.all()
    return render(request,"mate/stlist.html",{'stlist':stlist})
    
def signup(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        birthday=request.POST.get("birthday")
        age=request.POST.get("age")
        
        Student(name=name,email=email,birthday=birthday,age=age).save()
        return redirect("mate:list")
    return render(request,"mate/signform.html")
    
def detail(request,id):
    stlist = Student.objects.get(pk=id)
    return render(request,"mate/detail.html",{'stlist':stlist})
    
def update(request,id):
    stlist = Student.objects.get(pk=id)
    if request.method == "POST":
        stlist.name=request.POST.get("name")
        stlist.email=request.POST.get("email")
        stlist.birthday=request.POST.get("birthday")
        stlist.age=request.POST.get("age")
        stlist.save()
        return redirect("mate:list")
    return render(request,"mate/update.html",{'stlist':stlist})

def delete(request,id):
    stlist = Student.objects.get(pk=id)
    stlist.delete()
    return redirect("mate:list")