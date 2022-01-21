# my car.py
from vehicle import Car  #vehicle 파일안에 car만 사용하겠다! 


if __name__ == '__main__':
    mycar = Car('98하 5678','흰색') 
    #mycar.차량번호 = '98하 5678'
    #mycar.색상 = '흰색'
    mycar.연료 = '경유'
    mycar.__제조사 = '기아'
    mycar.출고년도 = 1999
    # mycar.기어단수 = 7


    print(mycar.__제조사)
    print(mycar.연료)
    # print(mycar.기어단수)
    mycar.set제조사('쌍용')
    mycar.제조사확인()

    mycar.전진한다(2)
    print(mycar)

