
### 실습_미세먼지 농도를 받아 좋고, 나쁨 현재 상태를 출력하세요
location = '서울'
time = '2018-12-20'
dust = 48

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