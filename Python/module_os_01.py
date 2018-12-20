#파일 이름 변경하기
#OS==============================================================
import os

os.chdir(r'C:\Users\student\Downloads\work\SSAFY지원자')

for filename in os.listdir("."):
    os.rename(filename,"SSAFY_"+filename)

