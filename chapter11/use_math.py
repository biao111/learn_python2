import re

#将正则表达式编译
pattern = re.compile(r'hello',re.I)
print(dir(pattern))

#通过match进行匹配
rest = pattern.match('Hello, world!')
print(rest)
print(dir(rest))
print('string:',rest.string)
print('re:',rest.re)
print(rest.groups())