## Python_예제__print

### 기본_"안녕~!"을 찍어보자

```python
#1
print("안녕~!")

#변수를 이용해보자
a="안녕"
print(a)

#리스트를 이용해보자
b=["안녕","hi","오하이요"]
print(b[0])

#딕셔너리를 이용해 안녕 표현의 언어를 프린트 해보자
c={'안녕':'한국', 'hi':'미국','오하이요':'일본'}
print(c['안녕'])
```



### 실습_메뉴를 말해주는 chatbot 만들기

```python
import random

menu=['닭','삼겹살','국수','빵','비빔밥']
pick=random.choice(menu)

print(pick)
```



### 실습_딕셔너리를 이용해서 점심메뉴 가게 전화번호를 보여주세요

```python
import random

menu=['닭','삼겹살','국수','빵','비빔밥']
phonenumber={'닭':'010-111-1111','삼겹살':'010-222-2222','국수':'010-333-3333','빵':'010-444-4444','비빔밥':'010-555-5555'}
pick=random.choice(menu)

print(pick)
print(phonenumber[pick])
```







## 조건; if / elif / else

### 실습_미세먼지 농도를 받아 좋고, 나쁨 현재 상태를 출력하세요

```python
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=' + key + '&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)
stat =""

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))

if(dust<15):
  stat="좋음"
elif(dust>16 and dust<50):
  stat="보통"
elif(dust>51 and dust<100):
  stat="나쁨"
else :
  stat="매우 나쁨"
print("현재 미세먼지 농도는 %d 이고 현재상태 %s"% (dust, stat))
```







## 반복; while / for

### 실습_for문을 써서 'go' 4번 출력해보세요

```python
for i in range(1,5):
    print('go')
```



### 실습_숫자 45개 중 로또 숫자 5개를 뽑아보자

```python
import random

lotto=range(1,46)  #range는 range(1,46) **오른쪽 숫자보다 1 작은 수까지 수열 결과 보여준다.**
lotlist=random.sample(lotto,5)

print(lotlist)
```





---

### 심화_공공데이터 활용 미세먼지 봇 만들기

```python
#숙제^^
```



[^공공데이터포털]: 기타 공공데이터를 받을 수 있는 사이트
[^requests]: 데이터 받는 파이썬 모듈
[^BeautifulSoup]: parser 모듈 함수 크롤링 할때 좋음
[^자소설닷컴]: IBM personal Insight
