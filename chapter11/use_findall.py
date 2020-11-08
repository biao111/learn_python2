import re

content = 'one1tow22three333four4444five5six698'
p = re.compile(r'\d+')

#使用编译的对象
rest = p.findall(content)
print(rest)