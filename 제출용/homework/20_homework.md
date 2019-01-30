# 데이터베이스 관계(1:N)

### 학습해야 할 내용

- 1:N 관계



1. Class 모델과 Student 모델을 1:N관계로 설정하려고 한다. models.py에 넣어야 하 는 코드를 작성하세요. (1:N관계중 N의 클래스를 작성해주세요)



**정답 :**

```python
class Student(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    
    def __srt__(self):
        return self.content    
```





2.  Question 모델과 Comment 모델은 1:N관계를 가지고 있다.

   A = Question.objects.get(id=id)

   위의 코드가 있을때 views.py에서 Comment를 모두 가져오기 위한 코드를 작성하세요.

   (related_name 은 설정하지 않았다고 가정한다.)



**정답 :**

```python
comment = Comment.objects.filter(question=A.id)
```





3. 기본적으로 1:N관계를 설정을 할때 ForeignKey를 이용해서 1에 해당하는 클래스 를 지정해준다.

   지정한 클래스가 Movie일때 ForeignKey로 지정된 컬럼의 이름은 무엇인가?



**정답 : **

```python
id
```



