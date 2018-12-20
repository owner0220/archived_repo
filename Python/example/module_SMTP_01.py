#SMTP==============================================================
import smtplib
import getpass
from email.message import EmailMessage

idi = getpass.getuser()
password = getpass.getpass('비밀번호뭐니?')

smtp_url = "smtp.naver.com"
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url,smtp_port)
s.login("로그인 이메일",password)

msg = EmailMessage()
msg['Subject'] = "test"
msg['To'] = "받는 이메일"
msg['From'] = "보내는 이메일"

msg.add_alternative('''
    <title>안녕하세요</title>
    <h1>밥시간 이에요!!</h1>
    <p></p>
    ''',subtype="html")        
s.send_message(msg)