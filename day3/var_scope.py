#변수의 라이프 스코프

a = 1  #전역변수(Global)_전체에 사용할 수 있음  #_4번행에 위치한 a와 완전 다른 a 

def vartest(a): #지역변수(local) (함수선언 'def' 실행되는 것이 아님)
    a = a + 1
    return a

a = vartest(a) #2번행에 있는 a와 같음
print(a)







