from django.urls import path
from . import views
app_name="mate"
urlpatterns = [
    path('', views.stlist,name="list"),
    path('signup/', views.signup,name="signup"),
    path('<int:id>/detail/', views.detail,name="detail"),
    path('<int:id>/delete/', views.delete,name="delete"),
    path('<int:id>/update/', views.update,name="update"),
    
]
