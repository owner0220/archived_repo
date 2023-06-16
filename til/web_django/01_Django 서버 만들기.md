>PYTHON ver 3.6.7
>
>Linux / bash 창 /  c9.io 환경

[TOC]

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



## Django Project 폴더 안의 파일에서 설정

### 3. Django  Setting

#### Templates 위치, 접속 허용, 요청과 처리 설정

##### 1)  **settings.py**

- **TEMPLATES_DIR 위치변수 설정**

  

  - **BASH_DIR 변수 밑에 TEMPLATES_DIR 변수 선언**

    ```bash
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATES_DIR = os.path.join(BASE_DIR,"templates")
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



---

여기까지 다 만들었다면 서버로 실행 가능

## 서버 실행

```bash
python manage.py runserver $IP:$PORT
```

입력 실행