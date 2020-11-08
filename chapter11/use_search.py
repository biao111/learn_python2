import re

content = 'hello world!'

p = re.compile(r'world')
#使用search
rest = p.search(content)
print(rest)

#使用match
rest_match = p.match(content)
print(rest_match)
#match 从开头去找，第一个没找到就算了
#search 从开头一直找