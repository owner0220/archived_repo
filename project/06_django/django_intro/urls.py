from django.urls import path,include
from . import views

app_name = "movies"

urlpatterns = [
    path('',views.mlist,name="list"),
    path('<int:id>',views.mdetail,name="detail"),
    path('<int:id>/delete',views.mdelete,name="delete"),
    path('<int:id>/update',views.mupdate,name="update"),
]
