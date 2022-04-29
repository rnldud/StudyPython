# 부산버스 노선별 이용건수
import csv
from fileinput import filename 

file_name = '부산버스정보.csv'
f = open('부산버스정보.csv',mode = 'r', encoding = 'utf-8' )

reader = csv.reader(f, delimiter = ',')  
next(reader) #헤더를 없애는 역할
for line in reader:
    print(line)

f.close()