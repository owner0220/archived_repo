# 플라스크

[TOC]

### 사용법

#### 1. 파이썬 파일 작성하기

##### Python (.py )  코드

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
```



#### 2. bash창 에서 입력하고 실행하는 코드

```bash
FLASK_APP=위 파이썬파일이름.py flask run --host=아이피주소 --port=포트번호
```



- ##### 실행 예)

  - ```bash
    FLASK_APP=app.py flask run --host=127.0.0.1 --port=8080
    ```

  - ```bash
    FLASK_APP=ok.py flask run --host=222.127.1.1 --port=8080
    ```

