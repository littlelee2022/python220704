# DemoOS.py
from os.path import *

#print(dir())

print(abspath("python.exe"))

print(basename("c:\\work\\python.exe"))

print(exists("c:\\python39\\python.exe"))

print(getsize("c:\\python39\\python.exe"))

from os import *
#system("notepad.exe")
print("운영체제:", name)


#파일 목록
import glob
result = glob.glob("c:\\python_work\\*.py")

for item in result:
    print(item)