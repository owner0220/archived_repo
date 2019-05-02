# JS DOM 조작과 JS 응용

### Background

- JS 기초 문법 학습
- 기존 Python 코드의 추상화 된 핵심 이해

### Goal

- Python 기초 개념 코드를 JS 코드로 번역

### Problem

- 아래 Instruction에 따라 JS 코드로 작성해 보자.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Clicked</title>
</head>
<body>
<h1>0</h1>
<button id="change-btn">Click it</button>
<script>
// #change-btn 을 button 상수에 할당한다.
    const button = document.getElementById('change-btn');
// h1 태그를 header 상수에 할당한다.
    const header = document.getElementsByTagName('h1')
// clickCount 변수를 0으로 초기화 한다.
    let clickCount = 0
// button에 'click' eventListner를 추가한다. 클릭이 일어나면, 
    button.addEventListener('click',function(){
// clickCount 가 1씩 올라간다.
// header 안의 내용을 clickCount 로 바꾼다.
        header.innertext = ++clickCount;
    });

</script>
</body>
</html>
```





