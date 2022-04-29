# #웹페이지 긁어오기 
#   ## web이란 request에 대한 response
# from urllib.request import Request, urlopen 


# req = Request('https://www.naver.com') #네이버 웹페이지를 요청
# res = urlopen(req)

# print(res.status)  #결과값 200: 웹브라우저 가져오기 성공/ ~~404 도출 시 페이지 발견 실패

#외부 request 패키지 추가 설치
# pip install requests 

import requests
url = 'https://www.naver.com'
res = requests.get(url)

# print(res.status_code)
print(res.text)
