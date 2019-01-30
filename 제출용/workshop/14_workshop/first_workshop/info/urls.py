from django.urls import path
from . import views

urlpatterns = [
    path("", views.info),
    path("<str:stname>/", views.read),
]
