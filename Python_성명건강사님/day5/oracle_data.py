# oracle_data
# cx_oracle : pip install cx_oracle
from sqlite3 import DatabaseError
import cx_Oracle as ora

#makedsn('호스트명/ip주소', portnum, '서비스명') # 포트(=도로의 차선과 같음/오라클:1521 mysql:3306)
dsn = ora.makedsn('localhost', 1521, service_name ='orcl')  #dsn= datasourcename /  localhost = 내컴퓨터를 뜻하는 단어
#connect(user, password, dsn, encoding)
conn = ora.connect(user = 'scott', password = 'tiger', dsn=dsn, encoding='utf-8')

cur = conn.cursor()  #cur 마우스 포인트랑 같음/ 테이블을 지시

try:
    # for row in cur.execute('SELECT * FROM emp'):  #쿼리를 가져와 사용할 시 (SELECT * FROM EMP 뒤 ';') 사용시 예외발생 21,22행 참고
    #     print(row)
    
    cur.execute('SELECT COUNT(*), \'sample\' FROM emp')
    result = cur.fetchone() # fetchone()은 한번 호출에 하나의 Row 만을 가져올 때 
    print(result)

# cur.close()   # 커서부터 먼저 클로즈.
# conn.close()  # 접속 닫음
#데이터를 보면 기본적으로 변환할 수 없는 튜플형식

except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 13번라인 확인요: {e}')
finally:
    cur.close() #커서 닫고
    conn.close() #접속 닫음