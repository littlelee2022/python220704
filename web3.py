# web2.py

#웹서버에 요청

import urllib.request

#크롤링
from bs4 import BeautifulSoup

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
    print("웹 크롤링 종료")
except:
    pass