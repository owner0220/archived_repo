from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('movies/', include("movies.urls")),
    path('posts/',include("posts.urls")),
    path('', views.top_rank),
    path('api-auth/', include('api_v1.urls')),
    
]
