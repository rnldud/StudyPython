# exception_handle.py
# 예외처리!! 가장 중요!!!!!

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiple(a, b):
    return a * b

def divide(a, b):
    return a / b

print('사칙연산 시작')    
a, b = 4, 1             #오류: 빨간 줄(실행 전), 예외: 실행 중 발생 오류 (0입력시)
numbers = [3, 6, 9]  #임의의 리스트 생성

try: 
    print(f'나누기 결과 : {divide(a, b)}')
    res = int(numbers[1]) * 8
    num = int(input('수를 입력하세요'))
    
except ZeroDivisionError as e:  #as e: ZeroDivisionError의 축약형(예외 객체명을 정확히 작성)
    print(f'나누기 예외. 추가처리1 {e}')    # exception 중 zeroDivisionError (exception은 예외도 존재 무조건 작성x)
except IndexError as e:
    print(f'인덱스 예외. 추가처리2 {e}')
except ValueError as e:
    print(f'제발! 숫자만 넣어주시오')
except Exception as e:
    print(f'알수없는 예외. 추가처리5 {e}')

finally: #무조건 처리(예외발생해도)
    print(f'곱하기 결과 : {multiple(a, b)}')
    print(f'빼기 결과 : {minus(a, b)}')
    print(f'더하기 결과 : {add(a, b)}')

print('사칙연산 종료')