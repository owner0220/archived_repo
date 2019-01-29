>PYTHON ver 3.6.7
>
>Linux / bash 창 /  c9.io 환경

# Django 서버 만들기

### 1. Django 설치

- bash 창에 아래 코드를 입력해 Django를 설치한다.

```bash
pip install django
```





### 2. Django Project 만들기

- bash 창에 아래 코드를 입력하면서 프로젝트이름은 원하는 데로 지정하면 된다.

- ```bash
  django-admin startproject 프로젝트이름
  ```

  - 실행하면 코드를 실행한 폴더에 프로젝트 이름의 폴더가 만들어지면 성공



### 3. Django App 만들기

- bash  창에 입력 앱 이름은 원하는 데로 지정!

- ```bash
  django-admin startapp 앱이름
  ```

  - 실행하면 실행한 폴더에 앱이름의 폴더가 만들어지면 성공

    ※ 반드시 Project 파일 안에 app 이 들어 있어야 한다.





---



## Django Project 폴더 안의 파일에서 설정

### 4. Django  Setting

#### Templates 위치, 접속 허용, 요청과 처리 설정

##### 1)  **settings.py**

- **TEMPLATES_DIR 위치변수 설정**

  

  - **BASH_DIR 변수 밑에 TEMPLATES_DIR 변수 선언**

    ```bash
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATES_DIR = os.path.join(BASE_DIR,"template")
    ```

  

  

  - **TEMPLATES 참조 위치 입력**

    이 변수를 중간쯤 위치한 TEMPLATES 리스트의 'DIRS' 안에 넣어준다.

    ```bash
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATES_DIR],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```



- **접속 허용 설정**

  - ALLOWED_HOSTS = ['*']

  ※ 리스트 안에는 접속 허용하는 IP 주소를 넣으면 된다.



- **만든 Django App을 등록**

  - ```bash
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'tt'
    ]
    ```

    ※ 나는 tt 라는 이름의 Django App 을 만들었기에 tt를 추가



##### 2) urls.py

- 인터넷 url 요청에 대한 응답을 바인딩 해준다.

  ```bash
  from django.contrib import admin
  from django.urls import path, include 
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path("tt/", include("tt.urls")),
  ]
  ```

- 내용 : 인터넷으로 **서버주소/tt** 이렇게 접속하면  그 결과는 tt 앱의 urls에서 처리하겠다!!

---



## Django App 폴더 안의 파일에서 설정

### 5. Django App  Setting

#### 앱으로 오는 요청과 처리, 그에 따른 화면 연결  |  view 제작, 연결

##### 1) urls.py

```bash
from django.urls import path
from . import views

urlpatterns = [
    path("", views.hi),
]
```

- 내용 : Django Project에서 include("tt.urls") 로 보내서 들어온 요청을 views에서 hi 메서드를 통해 처리



##### 2) views.py

```bash
from django.shortcuts import render

# Create your views here.
def hi(request):
    return render(request,"index.html")
```

- 내용 :  hi 를 실행하면  index.html 로 보여줘라~! 이때 이 html 파일은 **templates** 폴더 안에 만들어 둬야한다.



##### 3) Django App 폴더 안에 templates 폴더 만들기 그리고 html 파일 만들기

```bash

```





---

여기까지 다 만들었다면 서버로 실행 가능

## 서버 실행

```bash
python manage.py runserver $IP:$PORT
```

입력 실행