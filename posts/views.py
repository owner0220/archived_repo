from django.shortcuts import render,redirect
from .forms import Postform

# Create your views here.
def list(request):
    return render(request,"posts/list.html")
    
    
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
    return render(request,'posts/create.html',{'form':form})
    