from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_page,name="movie_page"),
    path('new/', views.movie_new,name="movie_new"),
    path('<int:movie_pk>', views.movie_detail,name="movie_detail"),
    path('<int:movie_pk>/edit', views.movie_edit,name="movie_edit"),
    path('<int:movie_pk>/scores/new', views.scores_new,name="scores_new"),
    
]
