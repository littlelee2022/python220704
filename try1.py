# try1.py

# 함수 정의 
def divide(a,b):
    return a/b

try:
    #함수 호출
    result = divide(5,"ㅂㅂㅂ")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
except TypeError:
    print("숫자이여야 합니다")
else: 
    print("결과 : {0}".format(result))

finally:
    print("무조건 한번 더 실행")


print("전체 코드 실행 종료")