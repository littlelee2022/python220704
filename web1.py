# web1.py

# 웹 클롤링(웹 데이터 수집 기술)
from bs4 import BeautifulSoup

# 문서 로딩
page = open("C:\\python_work\\test01.html","rt",encoding="utf-8").read()

#검색이 용이한 객체 (두가지 가능 : html.parser, xml.parser) 
soup = BeautifulSoup(page,"html.parser")
# print(soup.prettify())

#문서의 <p> 모두 검색 ==> 리스트 
# print(soup.find_all("p"))
# print(soup.find_all("a"))

#첫번째 <p> 검색 ==> 처음 나오는 것에서 멈춘다.
# print(soup.find("p"))

#<p class=outer-text>: 약간의 검색 조건
#print(soup.find_all("p",class_="outer-text"))

# 문자열만 추출
for item in soup.find_all("p",class_="outer-text"):
    #내부를 삭제하고 내부 컨텐츠만 리턴
    title = item.text
    print(title.strip())