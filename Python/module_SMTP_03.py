#SMTP2==============================================================
import smtplib
import getpass
from email.message import EmailMessage

password = getpass.getpass('비밀번호뭐니?')


msg = EmailMessage()
msg['Subject'] = "Title of mail"
msg['From'] = "a@naver.com"
msg['To'] = "qweqwe@ruu.kr"
msg.set_content('This is contents')

smtp_url = "smtp.naver.com"
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url,smtp_port)
s.login('a',password)
s.send_message(msg)