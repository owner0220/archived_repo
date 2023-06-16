# 파이썬에서 SQL DB 사용하기

### SQLalchemy

[TOC]

### 사용법

#### 1. 파이썬 파일 작성하기

**※ 이 파일의 이름은 꼭 ```wsgi.py``` 이거나 ```app.py``` 이여야 한다.**

##### Python (.py) 코드

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)

migrate = Migrate(app,db)

@app.route("/")
def hello():
    return "Hellow"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
```





#### 2.  1번의 파이썬 코드가 들어 있는 곳에서 bash 창을 열고 아래의 코드를 실행

​	1) ```flask db init```        : db 만들기

​	2) ```flask db migrate```  : db 스키마데로 테이블 만들고 파이썬과 db를 연결해주기

​	3) ```flask db upgrade```  :  db 최신버전으로 업그레이드 해주기

**※ 여기 명령어에서 db는 위 코드와는 상관 없이 정해진 명령어이다.**

성공하면 지금 폴더에 migrations 폴더가 생기면서 versions 안에 어떤 이름의 .py 파일이 생긴다.





### **코드 설명**

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

# sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 여기서 사용할 db를 만들어준다. 여기서는 'db' 라는 이름으로 만들었다.
db = SQLAlchemy(app)
# sqlalchemy 초기화
db.init_app(app)

# sql에서 사용할 db table 스키마 만들기=============================================
class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
# 테이블 이름은  todos
# id INTEGER, title String(20),  content String(100), created_at DateTime
# 
# SQL 쿼리 문으로는 아래와 같은 테이블 생성하겠다고 클래스로 만들어 놓았다.
# CREATE TABLE todos (
# id INTEGER PRIMARY_KEY, 
# title TEXT,
# content TEXT,
# created_at DATETIME);
# ==============================================================================


# 위의 스키마 데로 지금 폴더 안에 파이썬과 SQL을 연결해주는 명령 코드를 자동으로 생성하도록
# 연결해주는 한줄
migrate = Migrate(app,db)
    
@app.route("/")
def hello():
    return "Hellow"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
```





