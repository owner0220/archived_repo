from django import forms
from .models import Post,Image,Comment

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]
        widgets = {
            'file' : forms.FileInput(attrs={'multiple':True})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]