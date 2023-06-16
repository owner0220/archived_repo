from django.urls import path
from . import views

app_name = 'intro'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('html/', views.HtmlView.as_view(), name="html"),
    path('hello/<str:name>/', views.HelloView.as_view()),
    
]