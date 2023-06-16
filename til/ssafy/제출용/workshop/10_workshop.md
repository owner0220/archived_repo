# CSS

### Background

- HTML

### Goal 

-  CSS Selector 를 이해한다
-  CSS 프로퍼티를 이해한다.



### Problem

1. Selector 를 활용한 DOM 탐색 실습. 

```html
<!--nth child는 타입 구분 없이 위에서 부터 순서대로 몇 번째를 선택하는 것이다.-->
<style>
    #ssafy > p:nth-child(2){
        color: red;
    }
    #ssafy > p:nth-of-type(2){
        color: blue;
    }
</style>
<!--nth-of-type()은 타입 구분 하면서 : 앞의 태그의 순서 몇 번째를 선택하는 것이다.-->
```