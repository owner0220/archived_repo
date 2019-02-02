"""urlshorter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #데이터 베이스에 접속할수 있는 admin 페이지
    path('admin/', admin.site.urls),
    #Url을 줄여서 저장하고 처음페이지로 돌려준다.
    path('shorter/',views.shorturl),
    #첫 페이지
    path('', views.first),
    #외부에서 줄여진 url을 사용했을때 그에 해당하는 페이지 찾아서 리다이렉트
    path("<str:shorturl>/",views.red),
]
