from tkinter import *
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class Guit():
    def __init__(self):
        self.tkhandler = Tk()
        self.tkhandler.geometry('500x500')
        self.tkhandler.title('네이버 블로그 검색 프로그램')

        # Label를 사용해서 어디에 사용할 건지 명시, 그리고 무엇을 명시할 것인지 내용 씀
        self.label_title = Label(self.tkhandler, text='네이버 이메일 추출')
        self.label_title.pack() # 한줄씩 쌓이게 함
        
        self.btn = Button(self.tkhandler, text='블로그 검색 시작', width=30, command=self.auot_11st) #버튼 누르면 auto-11st 함수와 연결
        self.btn.pack()

        self.label_start = Label(self.tkhandler, text = '시작점부터 100개 검색')
        self.label_start.pack()
        self.text_start = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
        self.text_start.pack()

        self.label_today = Label(self.tkhandler, text = '투데이 기준')
        self.label_today.pack()
        self.text_today = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
        self.text_today.pack()

        self.label_word = Label(self.tkhandler, text = '검색어')
        self.label_word.pack()
        self.text_word = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
        self.text_word.pack()

        self.scroll = Scrollbar(self.tkhandler, orient='vertical') #세로 스크롤 생성
        # 리스트 박스 안에서 스크롤하면 스크롤바도 움직일수 있게 연동해서 같이 움직임
        self.lbox = Listbox(self.tkhandler, yscrollcommand=self.scroll.set)
        # 스크롤바를 움직였을 때 왼쪽 리스트박스의 화면도 움직이게 연동
        self.scroll.config(command=self.lbox.yview)

        # 스크롤 위치
        self.scroll.pack(side='right', fill='y') #오른쪽에 전부 채움
        self.lbox.pack(side='left', fill='both', expand=True) #스크롤 제외 전부 채우고 화면 크기에 따라 expand된다

        self.append_log('프로그램을 시작합니다.')
        
    def auot_11st(self):
        self.append_log('검색을 시작합니다.')
        tid = self.text_word.get('1.0', END).strip() #get으로 입력된 text 가져오는데 1.0, END -> (첫번째 줄 0번째 단어부터 끝까지)
        start_point = self.text_start.get('1.0', END).strip() #get으로 입력된 text 가져오는데 1.0, END -> (첫번째 줄 0번째 단어부터 끝까지)
        today = self.text_today.get('1.0', END).strip() #get으로 입력된 text 가져오는데 1.0, END -> (첫번째 줄 0번째 단어부터 끝까지)
        // import requests
        // from urllib.parse import urlparse
        // from bs4 import BeautifulSoup
        # display 최대값이 100이므로 start값을 계속 100씩 추가해주면 됨.
        url = "https://openapi.naver.com/v1/search/blog?query=" + tid + '&start={}'.format(start_point) + '&display=100' # json 결과
        result = requests.get(urlparse(url).geturl(), headers={"X-Naver-Client-Id":"API 아이디",
        "X-Naver-Client-Secret": "API 비밀번호"})

        json_obj = result.json()
        # print(json_obj)
        # print(json_obj['items'])

        naver_id_list = []
        result = []

        for i in json_obj['items']:
            # print(i['bloggerlink'])
            a = i['bloggerlink']
            b = a[23:]
            naver_id_list.append(b)
            # print(b)
        print(naver_id_list)
        result_mail = []

        for naver_id in naver_id_list:
            res = requests.get('http://blog.naver.com/NVisitorgp4Ajax.nhn?blogId='+ naver_id)
            soup = BeautifulSoup(res.text, 'html.parser')

            a = soup.find_all('visitorcnt')
            sum = 0

            for i in a[0:len(a)-1]:
                sum += int(i['cnt'])
                # print(i['cnt'])
            
            if sum/4 >= int(today) and sum/4 <= int(today)+1500:
                print(naver_id,'의 지난 4일 투데이 평균: ', sum/4)
                result_mail.append(naver_id)

        result_mail = set(result_mail)
        print(result_mail)

        with open('C:/python_basic/test123123.txt','a') as f:
            for mail in result_mail:
                f.write(mail+'@naver.com,\n')

        self.append_log('검색을 종료합니다.')

    def append_log(self, msg):
        import datetime
        now = str(datetime.datetime.now())[11:-7]
        # listbox에 로그를 추가
        self.lbox.insert(END, '[%s] %s' %(now, msg))  # 리스트박스 맨마지막에 추가
        # gui에 변경이 일어나면 update해서 바로 반영할 수 있게
        self.lbox.update()
        # 메세지가 쌓여서 화면 밑까지 내려올때 스크롤 내려서 볼 수 있게 함
        self.lbox.see(END)


    def run(self):
        self.tkhandler.mainloop()

g = Guit()
g.run()