# Requests
# requests 사용 스크랩핑(2) - Json

# 공식 레퍼런스
# http://docs.python-requests.org/en/master/user/quickstart/

import json
import requests


s = requests.Session()

# 100개 Json 데이터 요청
r = s.get('http://httpbin.org/stream/100', stream=True)

# 수신 확인
# print(r.text)

# Encoding 확인
# print('Encoding : {}'.format(r.encoding))

# 데이터 타입 확인
# print(type(r))

# Encoding 타입 체크 후 UTF-8 변경
if r.encoding is None:
    r.encoding = 'UTF-8'

# 수신 데이터 -> Dict 변환
for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))
    
    # Json(Dict) 변환 후 타입 확인
    b = json.loads(line)
    # print(b)
    # print(type(b))
    
    # 정보 내용 출력
    for k, v in b.items():
        pass
        # print("Key: {}, Values: {}".format(k, v))
    # 줄 바꿈
    print()
    print()


s.close()


# r = s.get('https://jsonplaceholder.typicode.com/posts)
r = s.get('https://jsonplaceholder.typicode.com/posts/1')

# Header 정보
print(r.headers)
# 본문 정보
print(r.text)
# Json 변환
print(r.json())
# Key 반환
print(r.json().keys())
# Value 반환
print(r.json().values())
# 인코딩 정보
print(r.encoding)
# 바이너리 정보
print(r.content)

s.close()