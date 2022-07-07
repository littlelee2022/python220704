# DemoForm2.py

# DemoForm2.py(로직) + # DemoForm2.ui(화면단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

# 디자인 파일을 로딩(DemoForm2)
form_class = uic.loadUiType("DemoForm2.ui")[0] # <-- UI가 여려개있는 경우

# 폼클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 슬롯 메서드를 추가
    def firstClick(self):
        # 파일에 저장
        try:
            f = open("c:\\python_work\\webtoon.txt","wt",encoding="utf-8")
            for i in range(1,11):
                url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i)
                print(url)
                data = urllib.request.urlopen(url)
                soup = BeautifulSoup(data,"html.parser")

                # <td class="title">
                # <a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
                # </td> 

                cartoons = soup.find_all("td",class_="title")
                # print("갯수: {0}".format(len(cartoons)))
                # title = cartoons[0].find("a").text
                # link = cartoons[0].find("a")["href"]
                # print(title)
                # print(link)

                for item in cartoons:
                    title = item.find("a").text
                    print(title.strip())
                    f.write(title+"\n")

            f.close()
            # print("웹 크롤링 종료")
        except:
            pass
        self.label.setText("네이버웹툰 목록 크롤링 종료")
    def secondClick(self):
        
        self.label.setText("두번째 QT 데모~~")
    def thirdClick(self):
        self.label.setText("세번째 QT 데모~~")


# 진입점 체크
if __name__ == "__main__":
    #실행 프로세스 생성
    app = QApplication(sys.argv)
    # 화면 생성
    demoWindow = DemoForm()
    demoWindow.show()
    # 이벤트 대기
    app.exec() 
    