# M:N 관계

###  Background

- 데이터베이스 관계
- M:N 관계

### Goal

- M:N 관계 모델을 작성해본다.

### Problem

- 게시물의 해시태그를 구현하기 위하여 아래와 같이 객체-관계 다이어그램을 작성하였
  다. 다이어그램을 바탕으로 models.py 에 Post 모델과 Hashtag 모델을 정의해본다.

```python
from django.db import models

class HashTag(models.Model):
	content = models.CharField(max_length=100)
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    hashtags = models.ManyToManyField(HashTag,related_name="post",blank=True)
```

