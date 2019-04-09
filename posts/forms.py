from django import forms
from .models import Post,Image

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]
        widgets = {
            'file' : forms.FileInput(attrs={'multiple':True})
        }