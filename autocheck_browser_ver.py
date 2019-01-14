import os
import datetime
import intra

excutelogfile = open("출석.txt",'a',encoding='utf-8')
start = datetime.datetime.now()
excutelogfile.write(f"{start} ||  출근 출석 프로그램 시작\n")


#현재 시간이 8시 ~ 9시 사이면 실행해라   #이외에는 18시 01분 이후에 실행 시켜라
if 8 < start.hour <= 9 or (start.hour == 18 and start.minute >= 1):
    if intra.login():
        excutelogfile.write(f"{start.hour}:{start.min} ||  로그인 성공\n")
        if 8 < start.hour <= 9:  #출근 도장 찍고
            intra.incheck()
            excutelogfile.write(f"{start.hour}:{start.min} ||  출근 도장 꽝꽝\n")
        else:                    #퇴근 도장 찍고
            intra.outcheck()
            excutelogfile.write(f"{start.hour}:{start.min} ||  퇴근 ~!! 고생하셨습니다.\n")
    else:
        excutelogfile.write(f"{start.hour}:{start.min} ||  로그인 실패\n")
#그것을 제외한 다른 시간 일때는 그냥 종료
else:
    excutelogfile.write(f"{start} ||  프로그램이 종료 되었습니다.  \n") 


excutelogfile.close()
intra.browser.close()
