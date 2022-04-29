class Car:   #특성은 사용하기위해 작성함. class작성시 속성 필수~
    차량번호 = '22나 7777 '
    __제조사 = '현대'
    색상 = '흰색'
    연료 = '가솔린'
    출고년도 = 2018

    def __init__(self, 차량번호, 색상) -> None:
        self.차량번호 = 차량번호
        self.색상 = 색상

    def __str__(self) -> str:  #__str__ 매직메서드
        return f'제 차는 {self.출고년도}년에 만들어진 {self.연료} 차량입니다.'

    def 제조사확인(self):
        print(f'제조사 {self.__제조사}')
    
    #private 함수 
    def set제조사(self, 제조사): #값을 받아 할당을 해야지 제대로된 값 도출 
        self.__제조사 = 제조사   

    def 전진한다(self,level):
        print(f'{self.색상}차가 {level}단 으로 달린다')

    def 후진한다(self):
        print('뒤로 달린다')
    
    def 좌회전한다(self):
        print('왼쪽으로 달린다')
        
    def 우회전한다(self):
        print('오른쪽으로 달린다')       
    
    def 멈춘다(self):
        print('멈춘다')
        
