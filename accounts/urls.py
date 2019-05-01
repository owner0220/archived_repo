from django.urls import path,include
from . import views

app_name="accounts"

urlpatterns = [
    path('', views.account_list,name="account_list"),
    path('sign_up/', views.sign_up,name="sign_up"),
    path('sign_in/', views.sign_in,name="sign_in"),
    path('sign_out/', views.sign_out,name="sign_out"),
    
]
