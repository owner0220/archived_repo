# Django Form

###  학습해야 할 내용 

-  Form 클래스의 선언과 활용

1. Django Form을 활용하기 위해서 클래스를 만들때 장고 내부에 만들어져있는 클래스를 상속받아서 활용해야 한다. 이 클래스를 import 하는 문장을 작성하세요.



**정답 :**

```python
from django import forms


클래스는 forms.Form 을 상속 받는다.
```



2. 폼 클래스를 템플릿에서 활용하기 위해서 form이라는 이름으로 템플릿 페이지로 전달하였다. 템플릿 페이지에서 form을 <p>태그들로 감싸서 렌더링 하기 위한 코드를 작성하세요.



**정답 :**

```python
{{form.as_p}}
```



3. 폼 클래스를 활용할때 폼에 담긴 데이터가 유효한지 체크하기 위해서 is_valid() 메소드를 활용한다. is_valid() 메소드를 통과하고 나서 사용자의 데이터를 가져오 기 위해서 빈칸에 들어가야할 코드를 작성하세요.

```python
def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.00000000['name']
            age = form.000000000['age']
```



**정답:**

```python
cleaned_data
```

