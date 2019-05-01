from django.urls import path,include
from . import views
app_name="posts"

urlpatterns = [
    
    path('', views.post_lists,name="post_lists"),
    path('<int:m_id>/', views.post_detail,name="post_detail"),
    
]
