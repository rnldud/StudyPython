# While 문_반복수행
hit = 0

while hit < 100: #이값이 참인 동안
    hit += 1 #(hit = hit + 1) 동일 식
    #hit = hit + 1 #print 전 작성 시 0번째 표현x 순서확인

    if hit >10:
        break

    print(f'나무를 {hit}번 찍습니다')

#for문 변환 
for hit in range(1, 101): #('1번찍습니다' range(1,101)로변경 )

    if hit > 10:
        break

    print(f'나무를 {hit}번 찍습니다')

      
