# DemoRE.py

import re
# print(dir(re))


result = re.search("[0-9]*th","  35th")
print(result)
print(result.group())

result = re.match("[0-9]*th","  35th")
print(result)
#print(result.group())

print(bool(re.search("ap","this is apple")))
print(bool(re.match("ap","this is apple")))

result = re.search("\d{4}","this year is 2022")
print(result.group())

result = re.search("\d{5}","our country is 52300")
print(result.group())
