# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(2)

import requests
from lxml.html import fromstring, tostring


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인 함수
    """
    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL
    response = session.get('http://www.naver.com/')
    # 신문사 정보 딕셔너리 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)

    # 결과 출력
    for name, url in urls.items():
        print(name, url)


def scrape_news_list_page(response):
    # URL 딕셔너리 선언
    urls = {}
    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    # 문서내 경로 절대 경로 변환
    root.make_links_absolute(response.url)

    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
        # a 구조 확인
        # print(dir(a))

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

        # 신문사, 링크 추출 함수
        name, url = extract_contents(a)

        # 딕셔너리 삽입
        urls[name] = url
    return urls


def extract_contents(dom):
    # 링크 주소
    link = dom.get('href')
    # dom 구조 확인
    # print(tostring(dom, pretty_print=True))

    # 신문사 명
    name = dom.xpath('./img')[0].get('alt')  # xpath('./img')
    return name, link


#  스크랩핑 시작
if __name__ == '__main__':
    main()
