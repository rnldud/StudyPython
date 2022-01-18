# 함수 선언(선언은 바로 사용하는 것이 아님.불러줘야 사용됨) 및 사용

# 더하기 함수 선언
def add(a, b):
    res = a + b

    #모든함수는 return하기에 함수는 return이 필수적!
    return res 

# 함수 사용
print(add(2464,879))

mid_val = add(3, 4)
print(mid_val * 3)

print(add(6,4))  #동의어(argument,parameter,매개변수  add뒤 입력값)

# 함수 종류
# 매개변수(입력값) 없는 형태

def say_hello():
    return 'Hello~'

print(say_hello())
print(say_hello(), 'my friend')

val = say_hello()
print(val.replace('o~',''))

# 결과 값이 없는 형태
def say_hello(name):
    print(f'Hello~ {name}')
    #return None (None return시 생략가능)

say_hello('Hugo')


# 둘다 없는 경우
def say_goodbye():
    print('Bye bye~')

say_goodbye()

#매개변수 지정
def multi(a, b):
    return a * b

print(multi(2, 9))
print(multi(3, 19))


#매개변수 개수가 일정치 않은 경우
def plus(*args):
    res = 0

    for i in args:
        res += i

    return res

print(plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(plus(1, 2, 3, 4))


# 리턴값이 두개이상
def mul_and_div(x, y):
    mul = x * y
    div = x / y
    return (mul, div) # 튜플

(res1, res2) = mul_and_div(7 ,8)
print(res1, res2)


def 사칙연산(x, y):
    return (x+y, x-y, x+y, x/y)

res1, res2, res3, res4 = 사칙연산(9, 5)

print(res1, res2, res3, res4)
print(type(사칙연산(1, 2)))



