from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse
# Create your views here.

class Index(View):
    http_method_names = ['get']
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("안녕하세요!!!")

class HtmlView(TemplateView):
    http_method_names = ['get']
    template_name = 'intro/html.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hello'] = "change"
        return context
        
    
class HelloView(TemplateView):
    http_method_names = ['get']
    template_name = "intro/hello.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = kwargs.get('name')
        return context
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    