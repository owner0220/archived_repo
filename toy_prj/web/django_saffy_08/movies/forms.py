from django.forms import ModelForm
from .models import Genre,Movie,Score

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title','audience','poster_url','description','genre_id'
            ]
            
            
class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ['content','score',]