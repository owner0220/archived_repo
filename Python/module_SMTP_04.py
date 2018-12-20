#SMTP3==============================================================
import smtplib
import getpass
from email.message import EmailMessage
idi = getpass.getuser()
password = getpass.getpass('비밀번호뭐니?')

email_list = ['1@ruu.kr','2@ruu.kr']

for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = "Title of mail"
    msg['To'] = "qweqwe@ruu.kr"
    msg['From'] = email
    msg.set_content('This is contents')


smtp_url = "smtp.naver.com"
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url,smtp_port)
s.login(idi,password)
s.send_message(msg)