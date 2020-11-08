import re

'''
使用split正则分割字符串
'''

s = 'one1two22three333four4444five5six6'
p = re.compile(r"\d+")
rest = p.split(s,2)
print(rest)
