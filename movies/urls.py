from django.urls import path
from . import views

# app_name='movies'

urlpatterns = [
    # path('genres',views.genre_list,name='genre_list'),
    path('genres/',views.genre_list),
    path('genres/<int:genre_id>/',views.genre_detail),
    path('movies/',views.movie_list),
    path('movies/<int:movie_id>/',views.movie_detail),
    path('movies/<int:movie_id>/scores/',views.score_create),
    path('scores/<int:score_id>/', views.scores),
]

