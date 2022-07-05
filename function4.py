# function4.py
# 정의 되지 않은 인자(dict로 받기)

def userURIBuilder(server,port,**user):
    strURL = "http://"+server+":"+port+"/?"

    for key in user.keys():
        strURL += key+"="+user[key]+"&"
    return strURL

#호출
print(userURIBuilder("ycampus.com","80",id="kim",passwd="1234"))
print(userURIBuilder("ycampus.com","80",id="kim",passwd="1234",name="mike"))

#람다 함수(이름이 없는 함수)
g = lambda x,y:x*y

print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

# 반복 구문
value = 5

while value > 5:
    print(value)
    value -= 1

print("--구구단 출력--")
for x in  [2,3,4,5,6]:
    print("{0}단 출력".format(x))
    for y in range(1,10):
        print("{0} * {1} = {2}".format(x,y,x*y))


print("--break--")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i> 5:
        break
    print("Item:{0}".format(i))

print("--continue--")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 ==0 :
        continue
    print("Item:{0}".format(i))

print("--range--")
print(list(range(10)))
print(list(range(2000,2023)))
print(list(range(1,32)))

print("-- 리스트 컴프리헨션 --")
lst = list(range(1,11))
print([i**2 for i in lst if i>5])
tp = ("apple","banana","kiwi")
print([len(i) for i in tp])

print("-- 필터함수 --")
lst = [10,25,30]
iterL = filter(None,lst)
for i in iterL:
    print(i)

#함수정의
def getBiggerThan20(i):
    return i>20

print("-- 필터함수 적용 --")
lst = [10,25,30]
iterL = filter(getBiggerThan20,lst)
for i in iterL:
    print(i)

print("-- 람다함수 적용 --")
lst = [10,25,30]
iterL = filter(lambda x: x>20 ,lst)
for i in iterL:
    print(i)