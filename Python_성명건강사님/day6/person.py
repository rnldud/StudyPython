#person.py
#person 클래스
from codecs import getencoder


class Person: #사람을 뜻하는 명사는 변수가 된다. 
    name = '무명이' #아직 이름이 없다.  
    age = 0
    height = 0
    gender = ''
    feetsize = 0
    bloodtype = ''
    # pass #딱히 쓸말없고 뭘 작성해야할지 모를 때 pass~

    #생성자
    def __init__(self, name, age, height, gender) -> None: #None의 의미 = return값이 없음 '->'의 의미 = return값이 무엇인지 정확히 명시해주는것
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        print('Person이 생성되었습니다')





    #행위는 함수로 정의한다 (함수는 전부 동사)
    def 소개한다(self) -> None:
        greeting = f'''안녕하세요. 저는 {self.name} 입니다.
        {self.gender}구요. {self.age}살 입니다.'''

        print(greeting)

    def 먹는다(self, food):       
        print(f'{self.name}이(가) {food}을(를) 먹는다')
    def 일한다(self,drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다')

        #return(None)  #none값이기 때문에 생략
  
if __name__ == '__main__':   #시스템변수(컴퓨터상에서 이미 만들어져있음)/__init__ 은 함수
    guigui = Person('전귀영', 26 ,165, 'woman') # = __init__(self,name,age,height,gender)/ #person은 class인데 ()를 열면 함수가 됨. 
    # guigui.name = '전귀영'
    # guigui.age = 26
    # guigui.height = 165
    guigui.gender = '여성'
    guigui.feetsize = 240
    guigui.bloodtype = 'B'

    guigui.소개한다()
    guigui.먹는다('치킨')
    guigui.일한다('파이썬')


