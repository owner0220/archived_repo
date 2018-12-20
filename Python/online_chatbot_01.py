### 실습_미세먼지 농도를 받아 좋고, 나쁨 현재 상태를 출력하세요
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

