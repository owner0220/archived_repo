# JS DOM 조작과 JS 응용

### 학습해야 할 내용

- DOM 요소 선택과 조작
- EventListener 개념 이해

**1.** DOM에서 특정 요소를 선택할 때 document.querySelector() 뿐만 아니라  document.querySelectorAll() 역시 사용할 수 있다. 둘의 차이를 검색하여 기술하시오.

```javascript
document.querySelector()
특정 name, id 제한 없이 css 선택자를 사용해 요소를 찾는데
일치하는 것을 찾으면 검색을 중단하며 찾은 하나만 반환한다. 동일한 객체가 존재할 경우 html 문서 상위에 존재하는 요소를 반환한다.
```

```javascript
document.querySelectorAll()
콤마를 사용해 여러 요소를 한꺼번에 가져올 수 있다.
일치하는 모든 것을 검색하며 찾은 결과물을 모두 반환한다. 이때 반환객체는 nodeList이기 때문에 for 문 또는 foreach문을 사용해 꺼내야 한다. 
```







**2.** JS에서 자주 사용하는 EventListener 들 중 아래와 같은 것들이 있다.  각각 간략하게 어떤 Trigger를 의미하는지 조사하여 간략하게 기술하시오.

- click : 포인팅 장치 버튼이 엘리먼트에서 눌렸다가 놓였을 때
- mouseover : 포인팅 장치가 리스너에 등록된 엘리먼트나 그 자식 엘리먼트의 위로 이동했을 때
- mouseout : 포인팅 장치가 리스너가 등록된 엘리먼트 또는 그 자식 엘리먼트의 밖으로 이동했을 때
- mousemove : 포인팅 장치가 엘리먼트 위에서 이동했을 때(마우스가 이동하는동안 계속 실행됨)
- keypress : 쉬프트, Fn, CapsLock을 제외한 키가 눌린 상태일때 (연속적으로 실행됨)
- keydown : 키가 눌렸을 때
- keyup : 키 누름이 해제될 때
- load : 진행이 성공했을 때
- scroll : 다큐먼트 뷰나 엘리먼트가 스크롤되었을 때
- change : 변경되는 요소의 종류와 사용자가 요소와 상호 작용하는 방식으로 내용이 변경될 때





**3.** Dom에 요소를 추가할 때, innerHTML += 의 방법과 appendChild() 함수를 통해 추가하는 방법이 있다. 둘의 차이를 간략하게 기술하시오.

InnerHTML 은 **교체**

appendChild는 **추가**

속도는 InnerHTML이 약 2배 정도의 처리속도가 빠르다. 단, InnerHTML은 표준이 아며 appendChild는 표준이다.