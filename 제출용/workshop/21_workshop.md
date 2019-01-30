# 데이터베이스관계(1:N)

### Background

- ORM
- Django-model

### Goal 

- 1:N 관계에 대한 이해
- Django-modeling에 대한 이해



### Problem

1. 설문 앱을 만들려고 한다.

   이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇 표 를 받았는지 저장하는 기능을 가지고 있다.

   설문 앱은 Question 모델과 Choice 모델을 가지고 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고

   1:N 관계를 가지고 있다.

------

Question ; title 제목 CharField

Choice ; content 내용 CharField

​		votes 투표수 IntegerField

------



2. Question 하나를 보여주는 페이지에서 Choice를 위의 오른쪽 그림과 같이 출력하려 고 한다. html파일에서 내용과 투표수를 출력해주는 코드를 작성하세요. 현재 html파 일에는 아래와 같은 코드가 들어있다고 가정한다.

**정답 :**

```html
<h1>{{question.title}}</h1>
<ul>
    <li>한식 : {{question.comment_set.votes}}표</li>
</ul>
```



