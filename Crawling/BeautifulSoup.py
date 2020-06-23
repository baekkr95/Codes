# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(2) - 이미지 다운로드

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent

from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)]
# Header 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL(크롬 개발자 도구)
base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# 검색어
quote = rep.quote_plus("신소율")
# URL 완성
url = base + quote

# 요청 URL 확인
# print('Request URL : {}'.format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로
savePath = "C:/imagedown/"  # C:\\imagedown\\

# 폴더 생성 예외처리 (문제 발생 시 프로그램 종료)
try:
    # 기존 폴더가 있는지 체크
    if not (os.path.isdir(savePath)):
        # 없으면 폴더 생성
        os.makedirs(os.path.join(savePath))
except OSError as e:
        # 에러 내용
        print("folder creation failed!")
        print("folder name : {}".format(e.filename))
        
        # 런타임 에러 raise
        raise RuntimeError('System Exit!')
else:
    # 폴더 생성 정상일 경우 실행
    print('folder is created!')

# bs4 초기화
soup = BeautifulSoup(res, "html.parser")

# select 사용
img_list = soup.select("div.img_area > a.thumb._thumb > img")

# find_all 사용 할 경우
# img_list1 = soup.find_all("a", class_='thumb _thumb')
#
# print(type(img_list1))
# for v in img_list1:
#     img_t = v.find('img')
#     print(dir(img_t))
#     print(img_t.attrs['data-source'])

# 이미지 번호를 붙여주면서 다운로드
for i, img_list in enumerate(img_list, 1):
    # 속성 확인
    # print(img_list['data-source'])

    # 저장 파일명 및 경로
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
    # 파일명 출력 
    # print('full name : {}'.format(fullFileName))
    
    # 다운로드 요청(URL, 저장경로)
    req.urlretrieve(img_list['data-source'], fullFileName)

# 다운로드 완료 시 출력
print("download succeeded!")
