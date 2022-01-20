#커서에 접근하는 코드를 함수로 작성

from sqlite3 import Row
import cx_Oracle as ora

def myconn(): 
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8') #conn = 색상희미. 사용하지않았다는 것을 뜻함
    return conn #return값 작성시 색상 변함

def getAllData(conn): #conn객체를 매개변수 받아서 쿼리를 실행할 함수
    cur = conn.cursor() #커서 생성
    query = 'SELECT * FROM emp' #emp 테이블에서 데이터 모두 가져왕!
    for row in cur.execute(query): #emp 테이블의 최상단에 커서가 위치하면서 모든 데이터를 
        print(row) #한줄씩  출력

def getNameAndJobData(conn):
    cur = conn.cursor()
    query = 'SELECT ename, job FROM emp' #emp 테이블에서 ename,job 불러오기
   
    # for 문
    # for row in cur.execute(query): #emp 최상단에 커서가 위치하면서 모든데이터를 
    #     print(row) #한줄씩 출력
    
    #while 문
    cur. execute(query)
    while True: 
        row = cur.fetchone() #한 row(레코드) 읽기
        if row is None: 
            break
        else:
            print(row)


# def getDeptName(conn, no, loc):
#     cur = conn. cursor() # 커서를 conn에 생성.
#     query = f"SELECT * FROM dept WHERE deptno = {no} AND loc = '{loc}'" # dept 테이블에서 
#     cur.execute(query) # 한줄씩 읽기 위해 execute를 이용해서 실행시킨다. 
#     row = cur.fetchone() # 한줄씩 읽어라!
#     print(row)

def getDeptName(conn, tup):
    cur = conn. cursor() # 커서를 conn에 생성.
    #query = f"SELECT * FROM dept WHERE deptno = {tup[0]} AND loc = '{tup[1]}'" # '{tup[1]}' '' 사용이유: 문자이기때문에
    query = "SELECT * FROM dept WHERE deptno = :1 AND loc = :2" #오라클은 1부터 시작!
    cur.execute(query,tup)  #한줄씩 읽기 위해 execute를 이용해서 실행시킨다. 
    row = cur.fetchone() # 한줄씩 읽어라!
    print(row)



# def 부서명가져오기(연결객체, 받을수):
#     커서 = 연결객체.cursor()
#     쿼리 = f'SELECT * FROM dept WHERE deptno ={받을수}'
#     커서.execute(쿼리)
#     한줄 = 커서.fetchone
#     print(한줄)


#아래는 항상 맨밑부분에 작성해야함! # 메인프로그램이 시작될 것이다!
if __name__ == '__main__': #언더바 2개씩 #__name__: 시스템변수. name작성 시 main값 들어있음
    print('프로그램 시작')  #변수가 name이면 main을 시작
    # # 함수호출
    
    scott_con = myconn() #dsn, connect() 후 접속객체(conn)을 return 리턴/ 이 문장은 scot_conn,python,oracale을 연결

    no = input('1. 검색할 부서번호를 입력하세요:')
    loc = input('2. 지역명을 입력하세요: ').upper() #.upper 여기해도 상관없음
    tup = (no, loc)
    print(f'부서번호: {no} 지역: {loc}')
    getDeptName(scott_con, tup)

    # no = input('1. 검색할 부서번호를 입력하세요:')
    # loc = input('2. 지역명을 입력하세요: ').upper() #.upper 여기해도 상관없음
    # print(f'부서번호: {no} 지역: {loc}')
    # getDeptName(scott_con, no, loc)


    print('프로그램 종료')


    
    # print ('emp 테이블 전체 조회(SELECT *)')
    # getAllData(scott_con)

    # print('emp 2개 컬럼 조회')
    # getNameAndJobData(scott_con)
