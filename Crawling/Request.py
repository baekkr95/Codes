# Requests
# requests 사용 스크랩핑(1) - Session

import requests

# 세션 활성화
s = requests.Session()
# r = s.get('https://www.naver.com')

# 수신 데이터
# print('1', r.text)

# 수신 상태 코드
# print('Status Code : {}'.format(r.status_code))

# 확인
# print('OK? : {}'.format(r.ok))

# 세션 비활성화
# s.close()

s = requests.Session()

# 쿠키 Return
# r = s.get('http://httpbin.org/cookies', cookies={'name': 'niceman'})
# print(r.text)

# 쿠키 Set
# r = s.get('http://httpbin.org/cookies/set', cookies={'name': 'niceman'})
# print(r.text)

# User-Agent
# url = 'http://httpbin.org/get'
# headers = {'user-agent': 'niceman_app_v1.0.0'}

# Header 정보 전송
# r = s.get(url, headers=headers)
# print(r.text)

# 세션 비활성화
s.close()

# With 문 사용
with requests.Session() as s:
    pass
    # r = s.get('https://www.naver.com')
    # print(r.text)
