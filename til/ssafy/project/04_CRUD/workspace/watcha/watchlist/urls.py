from django.urls import path
from . import views

urlpatterns = [
    path("",views.movielist),
    path("<int:id>",views.mdetail),
    path("new/",views.mnew),
    path("create/",views.create),
    path("<int:id>/update",views.update),
    path("<int:id>/edit",views.update),
    path("<int:id>/delete",views.delete),
]
