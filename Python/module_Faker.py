import csv
from faker import Faker

f = open('1.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)

fake = Faker('ko_KR')

memset=[]
for i in range(60):
    fake_email = fake.ascii_safe_email()
    fake_name = fake.name()
    wr.writerow([fake_name,fake_email])
f.close()