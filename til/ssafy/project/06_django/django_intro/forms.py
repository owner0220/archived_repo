from django import forms
from .models import Movie

class PostForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        