# Django

### Background

- Django Web Framework
- Class Based View

### Goal

- Django Class Based View의 이해

### Problem

- cbv/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro/', include('intro.urls')),
    path('posts/', include('posts.urls')),
]

```

- posts/views.py

```python
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
    
```

- html

```html
{% extends 'posts/base.html' %}
{% block body %}
<h1>{{object.title}}</h1>
<h1>{{post.content}}</h1>
{% endblock %}
```

