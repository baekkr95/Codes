from selenium import webdriver
import telepot
import datetime
import os

# 로그 작성해서 어디에서 에러가 생겼는지 파악
def wirte_log(msg):
    f = open('C:/python_basic/Tkinter/auto.log', 'a')
    f.write('[%s] %s\n' %(str(datetime.datetime.now()), msg)
    f.close()


def do_auto(telegram_id='*********'):

    # write_log('제품 리스트를 가져옵니다.')

    f = open('products.txt', 'r')
    products = f.readlines()
    f.close()

    prices = None
    if os.path.exists('output.csv'):
        f = open('output.csv', 'r')
        prices = f.readlines().pop().strip().split(',')
        f.close()

    output = open('output.csv', 'a')

    # # 화면 ㄴㄴ
    # opts = webdriver.ChromeOptions()
    # opts.add_argument('headless')
    # driver = webdriver.Chrome('./chromedriver', chrome_options=opts)

    # wirte_log('크롬 브라우저를 시작합니다.')
    driver = webdriver.Chrome('./chromedriver')

    try:
        idx = 1
        header = ['']
        data = [str(datetime.datetime.now())]
        diff = []
        for url in products:
            url = url.strip()
            driver.get(url)

            elem = driver.find_element_by_class_name('heading')
            elem = elem.find_element_by_tag_name('h2')
            name = elem.text

            elem = driver.find_element_by_class_name('prdc_default_info')
            elem = elem.find_element_by_class_name('sale_price')
            price = elem.text.replace(',', '')

            if prices and price != prices[idx]:
                diff.append((name, prices[idx], price))

            header.append(name.replace(',', ''))
            data.append(price)

            idx += 1

        if diff:
            bot = telepot.Bot('*********')
            msg = ''
            for info in diff:
                msg += '- %s\n%s => %s\n' % info
            bot.sendMessage(telegram_id, msg)

        if not os.path.exists('output.csv'):
            output.write(','.join(header)+'\n')

        output.write(','.join(data)+'\n')
        output.close()

    except Exception as e:
        # wirte_log(e)
        print(e)
    finally:
        driver.quit()
