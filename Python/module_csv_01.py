#CSV 읽기
import csv

f = open('pygj - email.csv','r',encoding='utf-8')
read_csv = csv.reader(f)

for line in read_csv:
    print(line[0]+ '/' + line[1])
    
f.close()