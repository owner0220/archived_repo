## Python\_크롤링\_List_Out of range

와...나......이게 참..... 이거 하나 때문에 그 고생을..

### 환율정보 끌어오기

```python
# h.py 파일 내용
import requests
from bs4 import BeautifulSoup
url="https://ko.exchange-rates.org/MajorRates.aspx"
req = requests.get(url).text
soup = BeautifulSoup(req,"html.parser")
pick = soup.select("tbody > tr")
num=1
for tr in pick:
    ct=0
    print(tr.select("td")[0])
```

> Python 모듈 requests, bs4



### 결과창

bash 창에서  ```python h.py``` 입력 후 실행

```bash
student@DESKTOP MINGW64 ~/Downloads/work
$ python h.py
[]
[<td class="text-nowrapX"><a href="/currentRates/F/ZAR" title="ZAR"><i class="flag"><span class="za"></span></i></a><a href="/currentRates/F/ZAR" title="ZAR">남아프리카 랜드</a><br/></td>, <td>78.54646</td>, <td>0.06954</td>, <td>0.06131</td>, <td>7.82837</td>, <td>0.05509</td>, <td>0.09670</td>, <td>0.54354</td>, <td>0.09318</td>]
[<td class="text-nowrapX"><a href="/currentRates/P/HKD" title="HKD"><i class="flag"><span class="hk"></span></i></a><a href="/currentRates/P/HKD" title="HKD">홍콩 달러</a><br/></td>, <td>144.50804</td>, <td>0.12793</td>, <td>0.11280</td>, <td>14.40246</td>, <td>0.10135</td>, <td>0.17792</td>, <td>1.00000</td>, <td>0.17142</td>]

student@DESKTOP MINGW64 ~/Downloads/work
$ python h.py
Traceback (most recent call last):
  File "h.py", line 10, in <module>
    tr.select("td")[0]
IndexError: list index out of range
```



※ 결과창 첫줄 보면 **[]** 들어왔지... 그것 때문에 index out of range  떴어

코드 스펠링, 결과창 좀 자세하게 하나하나 보고 나서 구글링하자