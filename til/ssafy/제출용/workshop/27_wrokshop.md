# 사용자인증/사용자권한관리

### Background

- Django auth
- 1:1 관계

### Goal

- 사용자 인증을 활용한다.
- 유저정보를 저장하는 모델을 작성한다.

### Problem

```python
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields="__all__"
```

