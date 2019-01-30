# Bootstrap & Grid System

### 학습해야 할 내용

- Bootstrap
- Grid System



1. 다음은 부트스트랩의 어떤 component 이며 아래와 같이 만들려면 어떤 class를 주어야 하는가?

**정답 :**

```html
<button type="button" class="btn btn-danger">Danger</button>
```



2. 다음은 부트스트랩의 어떤 component 이며 아래와 동일하게 만들어 보시오.

```html
<div class="alert alert-primary" role="alert">Hello SSAFY ?!</div>
```



3. 다음 빈칸을 채우시오.

"부트스트랩 그리드 시스템은 레이아웃을    (      )개의 column으로   (        ) 개의 반응형 사이즈 조건을 사용하여 구축한다."

**정답 : 12, 5**

4. 아래와 같은 분할을 grid system 을 활용하여 만들어 보세요

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <style>
        div{
            border: solid 1px black;
        }
        .row {
            background-color: moccasin;
        }
    </style>
</head>
<body>
    <div class="row">
        <div class="col">25%</div>
        <div class="col-6">50%</div>
        <div class="col">25%</div>
    </div>
</body>
</html>
```

