# # if 구문 - 흐름제어
name = '영귀'
#name = ('명건', '태경',' 기영', '광조')

if name == '귀영' or name == '영귀':
#if '명건' in name:
    #print('호출자',name)   
    print('의사를 만나러 갑니다.')  #indent 들여쓰기 '#줄맞춤 필수
    print('의사쌤한테 인사합니다.')   
              
elif name =='다원':
    print('주사실로갑니다.')

else:
    print('호출할때까지 대기합니다.')           #name이 상이할 시 도출 

x = 2                   # '=' 값할당  '==' 동일값비교

if x != 10:
    pass
else:
    pass