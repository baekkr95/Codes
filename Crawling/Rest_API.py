# Requests
# requests 사용 스크랩핑(3) - Rest API

import requests

# Rest API GET, POST, DELETE, PUT:UPDATE, REPLACE (FETCH : UPDATE, MODIFY)
# https://jsonplaceholder.typicode.com/posts

# 세션 활성화
s = requests.Session()

# *예제1*
# 요청1
r = s.get('https://api.github.com/events')

# 수신 상태 체크
r.raise_for_status()  # 또는 status_code 체크

# 출력
print(r.text)

# *예제2*
# 쿠키 설정
jar = requests.cookies.RequestsCookieJar()

# 쿠키 삽입
jar.set('name', 'niceman', domain='httpbin.org', path='/cookies')


# 요청2
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 출력
print(r.text)


# *예제3*
# 요청3
r = s.get('https://github.com', timeout=5)

# 출력
print(r.text)


# *예제4*
# 요청4
r = s.post('http://httpbin.org/post', data={'kim': 'stellar'}, cookies=jar)

# 출력
print(r.text)

# 헤더 정보
print(r.headers)


# *예제5*
# 요청5(POST)
payload1 = {'name': 'kim', 'pay': 'true'}
payload2 = (('name', 'park'), ('pay', 'false'))

r = s.post("http://httpbin.org/post", data=payload2)

# 출력
print(r.text)


# *예제6*
# 요청5(PUT)
r = s.put('http://httpbin.org/put', data={'data': '{"name": "Kim", "grade": "A"}'})

# 출력
print(r.text)


# *예제6*
# 요청6(DELETE)
r = s.delete('http://httpbin.org/delete')

# 출력
print(r.text)


# *예제7*
# 요청7(DELETE)
r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)

s.close()
