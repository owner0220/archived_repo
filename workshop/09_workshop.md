# HTML

### Background

- Semantic Web

###  Goal 

-  HTML tag 를이해한다. 
-  Layout 구조를 이해한다.



###  Problem

1. 클릭하면 https://www.ssafy.com/ 로 이동하는 버튼을 만드시오

```html
<!--첫번째 정답-->
<a href=" https://www.ssafy.com/"><input type="button" href=" https://www.ssafy.com/"></a>

<!--두번째 정답-->
<button type="button" onclick="window.open('http://www.ssafy.com') ">
<!--세번째 정답-->
<button type="button" onclick="location.href='http://www.ssafy.com'">
```





2. 다음 태그에서 잘못된 부분을 찾으시오.

```<img href="https://www.google.com/" alt="GOOGLE">```

**정답**

이미지 경로이니까 src 를 사용해서 사용해야 한다.

```html
<img src="https://www.google.com/~~.png" alt="GOOGLE">
```



3.  당신은 현재 Resume.html 에서 작업중이다. “내 사진” 이라는 링크를 누르면
   Image 폴더 안에 my_photo를띄워주는 a 태그 경로를 넣으시오.

```html
<a href="../../Image/my_photo.png">내 사진</a>
```



