from django.forms import ModelForm
from .models import Genre,Score,Movie

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields=['name',]
        
class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields=['content','score',]
        
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields=['title','audience','poster_url','description',]