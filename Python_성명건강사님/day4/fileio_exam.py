# 파일입출력

#파일 출력_open & close 필수!
# f = open('newfile.txt', 'w') #w = write 쓰다, 파일출력과 같은 의미
# f.close()

# 특정경로에 파일생성
# f = open('C:/Sources/Sample/test.txt', 'w')
# f.close()
# print('파일이 생성되었습니다')

#ascii(영어만처리) cp949(한글처리) utf-8

# # newfile.txt 파일입력(읽어오기)
# f = open('newfile.txt', 'r' , encoding= 'utf-8')
# while True:
#     line = f.readline() #한줄씩읽기
#     if not line:
#         break
#     print(line)

# f.close()

f = open('newfile.txt', 'r' , encoding= 'utf-8')
# lines = f.readlines()
# print(lines)
# f.close()



for line in f:
    print(line.replace('\n',''))
f.close()