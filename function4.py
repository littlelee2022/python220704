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