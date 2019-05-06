from django.urls import path,include
from . import views
app_name="movies"

urlpatterns = [
    path('', views.movie_lists,name="movie_lists"),
    path('create/', views.movie_create,name="movie_create"),
    path('<int:id>/', views.movie_detail,name="movie_detail"),
    path('<int:id>/delete/', views.movie_delete,name="movie_delete"),
    path('<int:id>/update/', views.movie_update,name="movie_update"),
    path('test/<int:year>', views.movie_api_update,name="test"),
    
]
