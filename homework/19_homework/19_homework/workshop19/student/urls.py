from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    #Create
    path("new/",views.new),
    path("create/",views.create),
    #Read
    path("<int:id>/",views.read),
    #Update
    path("<int:id>/edit/",views.edit),
    path("<int:id>/update/",views.update),
    #Delete
    path("<int:id>/delete/",views.delete),
    
    ]