from django import forms
from .models import Hashtag, Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields=["content","post_img","post_geo","top",]
        #fields="__all__"
        widgets = {
            'file' : forms.FileInput(attrs={'multiple': True})
        }