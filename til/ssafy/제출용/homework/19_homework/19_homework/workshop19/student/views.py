from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def index(request):
    student = Student.objects.all()
    return render(request,"student/index.html",{"student":student})
    
def new(request):
    return render(request,"student/new.html")
    
def create(request):
    name = request.POST.get("name")
    email  = request.POST.get("email")
    birthday = request.POST.get("birthday")
    age = request.POST.get("age")
    # todo = Todo(title = title,content = content,due_date= due_date)
    # todo.save()
    
    Student.objects.create(name = name, email = email, birthday = birthday, age = age)
    
    return redirect("/student")
    
def read(request,id):
    student = Student.objects.get(pk=id)
    return render(request,"student/read.html",{"student":student})    
    
def delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect("/student")
    
def edit(request,id):
    student = Student.objects.get(pk=id)
    return render(request,"student/edit.html",{"student":student})
    pass

def update(request,id):
    student = Student.objects.get(pk=id)
    name  = request.POST.get("name")
    email = request.POST.get("email")
    birthday = request.POST.get("birthday")
    age = request.POST.get("age")
    print(age)
    
    student.name= name
    student.email = email
    student.birthday = birthday
    student.age = age
    student.save()
    
    return redirect(f"/student/{student.id}/")