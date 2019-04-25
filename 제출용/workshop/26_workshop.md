# Django Form

###  Background

- Django From

### Goal

- Form에 대한 이해
- HTML Form 만들기

### Problem

**1.**

```python
from django import forms
from .models import Student

class Postform(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'      

```

**2.**

```python
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block bb %}
<div class="container">
    <form class="mt-5" action="" method="post" enctype="multipart/form-data" accept="image/*">
        {% csrf_token %}
        {% bootstrap_form form %}
        <input type="submit"/>
    </form>
</div>
{% endblock %}
```

