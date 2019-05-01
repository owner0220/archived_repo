from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def movie_lists(request):
    return render(request,"movies/movie_list.html")