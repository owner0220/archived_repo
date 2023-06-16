from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class PostList(ListView):
    model = Post
    # template_name = "posts/asdf.html"
    
class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('posts:detail', kwargs={"pk":self.object.id})
        
class PostDetail(DetailView):
    model = Post
    
class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('posts:detail', kwargs={"pk":self.object.id})

class PostDelete(DeleteView):     
    model = Post
    success_url = reverse_lazy("posts:list")
    
    
    
    
    
    
    