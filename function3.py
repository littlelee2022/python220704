# function3.py
# 교집합 함수

from re import X


def intersection(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print(intersection("HAM","SPAM"))

#지역변수와 전역변수
x = 1
def func1(a):
    return a + x

#호출
print(func1(1))

def func2(a):
    x = 2
    return a + x
#호출 
print(func2(1))

print("----불변형식----")

a = 1.2
print(id(a))
a = 2.3
print(id(a))




print("----가변형식----")

lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))


# 객체는 참조를 통해 복사(입력+출력)
wordlist = ["J","A","M"]

#함수 정의 

def change(x):
    x[0] = "H"

def deepcopy_change(x):
    x1 = x[:]
    x1[0] = "H"
    print("내부", x1)
#호출
deepcopy_change(wordlist)
print("함수 호출 후 ", wordlist)

change(wordlist)
print("함수 호출 후 ", wordlist)

# 기본값
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

# 키워드 인자 방식
def connetURI(server,port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connetURI("ycampus.com","80"))
print(connetURI(port="8080", server="ycampus.com"))

#가변인자 처리
def union(*ar):
    result = []

    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM","EGG","SPAM"))