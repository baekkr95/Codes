# Selenium
# Selenium 사용 실습(4) - 실습 프로젝트(3)

import time
# 이미지 다운
import urllib.request as req
# 이미지 바이트 처리
from io import BytesIO

# 엑셀 처리 임포트
# import xlsxwriter
# bs4 임포트
from bs4 import BeautifulSoup
# selenium 임포트
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

# 엑셀 처리 선언
# workbook = xlsxwriter.Workbook("C:/crawling_result.xlsx")

# 워크 시트
# worksheet = workbook.add_worksheet()

# webdriver 설정(Chrome, Firefox 등) - 일반 모드
# browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))

# 제조사별 더 보기 클릭1
# Explicitly wait
WebDriverWait(browser, 3) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 제조사별 더 보기 클릭2
# Implicitly wait
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 클릭
WebDriverWait(browser, 2) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[14]/label'))).click()

# 2차 페이지 내용
# print('After Page Contents : {}'.format(browser.page_source))

# 3초간 대기
time.sleep(3)

# 현재 페이지
cur_page_num = 1

# 크롤링 페이지 수
target_crawl_num = 5

# 엑셀 행 수
ins_cnt = 1

while cur_page_num <= target_crawl_num:

    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # 소스코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 상품 리스트 확인
    # print(pro_list)

    # 페이지 번호 출력
    print('****** Current Page : {}'.format(cur_page_num), ' ******')
    print()

    # 필요 정보 추출(페이지 이동 크롤링)
    for v in pro_list:
        # 임시 출력
        # print(v)

        # 불필요한 영역 패스
        if not v.find('div', class_='ad_header'):
            # 상품명, 이미지, 가격
            prod_name = v.select('p.prod_name > a')[0].text.strip()
            prod_price = v.select('p.price_sect > a')[0].text.strip()

            # 이미지 요청 후 바이트 변환
            img_data = BytesIO(req.urlopen(v.select('a.thumb_link > img')[0]['data-original']).read())

            # 엑셀 저장(텍스트)
            worksheet.write('A%s' % ins_cnt, prod_name)
            worksheet.write('B%s' % ins_cnt, prod_price)

            # 엑셀 저장(이미지)
            worksheet.insert_image('C%s' % ins_cnt, prod_name, {'image_data': img_data})

            # 다음 행 증가
            ins_cnt += 1

        print()

    print()

    # 페이지 별 스크린 샷 저장
    browser.save_screenshot("c:/target_page{}.png".format(cur_page_num))

    # 페이지 증가
    cur_page_num += 1

    if cur_page_num > target_crawl_num:
        print('Crawling Succeed.')
        break

    # 페이지 이동 클릭
    WebDriverWait(browser, 2) \
        .until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page_num)))).click()

    # 소스코드 리로드
    # browser.refresh()

    # BeautifulSoup 인스턴스 삭제
    del soup

    # 4초간 대기
    time.sleep(4)

# 브라우저 종료
browser.quit()

# 엑셀 파일 닫기
workbook.close()
