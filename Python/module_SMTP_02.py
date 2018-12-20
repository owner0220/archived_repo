#SMTP1==============================================================
import csv
import smtplib
import getpass
from email.message import EmailMessage

idi = getpass.getuser()
password = getpass.getpass('비밀번호뭐니?')

f = open('pygj - email.csv','r',encoding='utf-8')
read_csv = csv.reader(f)
email = '보내는 메일'

smtp_url = "smtp.naver.com"
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url,smtp_port)
s.login(email,password)

i=0
for line in read_csv:
        msg = EmailMessage()
        msg['Subject'] = line[0] + " 님 이편지는"+str(i)+"번째 편지로 영국에서 최초로 시작되었습니다."
        msg['To'] = line[1]
        msg['From'] = email
        msg.set_content('이편지는영국에서최초로시작되어일년에한바퀴 돌면서 받는 사람에게 행운을 주었고지금은당신에게 로옮겨진이 편지는 4일 안에당신곁을 떠나야 합니 다.이 편지를 포함해서 7통을행운이 필요한 사람에게 보내 주셔야 합니다.복사를해도 좋습니다.혹 미신이 라하실지모르지만사실입니다. 영국에서HGXWCH이라는 사람은 1930년에 이편지 를받았습니다.그는비서에게 복사해서 보내라고 했 습니다.며칠 뒤에복권이당첨되어20억을 받았습니 다.어떤이는 이편지를받았으나96시간이내 자신의 손에서 떠나야 한다는 사실을 잊었습니다.그는곧 사 직되었습니다')
        s.send_message(msg)
        i+=1
f.close()