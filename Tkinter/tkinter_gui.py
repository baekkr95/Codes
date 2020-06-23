from tkinter import *

class Guit():
    def __init__(self):
        self.tkhandler = Tk()
        self.tkhandler.geometry('500x500')
        self.tkhandler.title('자동화 프로그램')

        # Label를 사용해서 어디에 사용할 건지 명시, 그리고 무엇을 명시할 것인지 내용 씀
        self.label_title = Label(self.tkhandler, text='안녕하세요 자동화 프로그램입니다.')
        self.label_title.pack() # 한줄씩 쌓이게 함
        
        self.btn = Button(self.tkhandler, text='11번가 조회', width=30, command=self.auot_11st) #버튼 누르면 auto-11st 함수와 연결
        self.btn.pack()

        self.label_telegram = Label(self.tkhandler, text = '텔레그램 ID')
        self.label_telegram.pack()

        self.text_telegram = Text(self.tkhandler, width=40, height=3, relief=RIDGE, bd=1)
        self.text_telegram.pack()

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
        self.append_log('예제를 시작합니다.')
        # example.py에 있는 do_auto 함수를 사용
        from example import do_auto
        tid = self.text_telegram.get('1.0', END).strip() #get으로 입력된 text 가져오는데 1.0, END -> (첫번째 줄 0번째 단어부터 끝까지)
        do_auto(tid)
        self.append_log('예제를 종료합니다.')
        
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