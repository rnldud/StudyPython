# # 기본 for문 - 반복적으로 처리 문장을 수행하는 것

arr = list(range(1, 100))
                 
for i in arr: 
     print(f'{i:1.1f}')

# 튜플로 for문

arr2 = ('me' ,'my' ,'friend' ,'jane')

for item in arr2:
    print(f'{item:>10}')  #10번째칸 오른쪽정렬 (콘솔에서 사용) ':>' : 정렬 공식  

# 합계 for문
numbers = list(range(1, 21, 2)) #1~20까지 홀수
res = 0 
for item in numbers:
     res += item  #+=변수에 더한 결과를 다시 변수에 할당

print(f'{numbers[-1]}까지의 총 합은 {res} 입니다.')

# 홀수 짝수 구분
numbers = list(range(1, 21)) #1~20까지 홀수

for item in numbers:
    if item % 2 == 0 : #짝수    ('!='로 변경하면 홀수)
        print(f'{item}은 짝수')

# 13이상이면 탈출_탈출 break 또는 계속continue
#break는 아예빠져나가는 것, continue는 수행하지않고 다음숫자로 

numbers = list(range(1, 21)) #1~20까지 홀수

for item in numbers:
    if item > 12 :
        break   #break 탈출,멈춰 (for문 바로 아래 작성해야함)

    if item % 2 == 1 : 
        print(f'{item}는 홀수')


for item in numbers:
    if item == 15 :
        continue  #15는 출력요망

    if item % 2 == 1 : 
        print(f'{item}는 홀수')
      
## 구구단 
for i in range(2, 10): #2 ~ 9까지 
    if i == 8:
        continue
    print(f'{i}단 시작')
    for j in range(1, 10): #1 ~ 9까지
        print(f'{i} x {j} = {i*j:2d}', end ='  ') #d: 값 공백  end: 현재 속한 출력물을 그 다음 출력값과 이어짐
    print('') #첫줄 print에 속함

for i in range(2, 10): #2 ~ 9까지 
    if i == 8:
        continue
    print(f'{i}단 시작')
    for j in range(1, 10): #1 ~ 9까지
        print(f'{i} x {j} = {i*j:2d}', end ='  ') #d: 도출된 값 공백  end: 현재 속한 출력물을 그 다음 출력값과 이어짐
    print('')

# inline for문
a = [1, 2, 3, 4]
result = [i * 3 for i in a]
print(result)

#기존 for문
t = []
for i in a:
    t.append(i * 3)

print(t)


