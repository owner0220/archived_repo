from django.urls import path,include
from . import views

app_name="posts"

urlpatterns = [
    
    path('', views.post_lists,name="post_lists"),
    path('create/', views.post_create,name="post_create"),
    path('<int:p_id>/', views.post_detail,name="post_detail"),
    path('<int:p_id>/create', views.post_create,name="post_create"),
    path('<int:p_id>/delete', views.post_delete,name="post_delete"),
    path('<int:p_id>/update', views.post_update,name="post_update"),
    
]
