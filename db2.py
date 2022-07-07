# db2.py

import sqlite3

#메모리에서 작업 : 약간의 약속된 문자열
# con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\python_work\\sample.db")

#커서 객체를 리턴
cur = con.cursor()

#데이터를 저장할 테이블 생성 : type이 5개 밖에 없다. int, text, float , blob, ??
cur.execute("create table PhoneBook(Name text, PhoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values ('derick','010-222');")

# 입력파라미터 처리
name = "gildong"
phoneNumber = "010-432"

cur.execute("insert into PhoneBook values (?,?);", (name, phoneNumber))

# 다중 레코드 입력(2차원 배열, 행열데이터)
datalist = (("tom", "010-345"),("dsp","010-333"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

#검색
cur.execute("select * from PhoneBook;")

# for row in cur:
#     print(row)

print("---fetchone()---")
print(cur.fetchone())

print("---fetchmany(2)---")
print(cur.fetchmany(2))

print("---fetchall()---")
print(cur.fetchall())

con.commit()
