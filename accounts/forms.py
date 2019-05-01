from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username',
            ]