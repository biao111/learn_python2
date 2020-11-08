import re

'''
使用正则表达式进行替换
'''
s = 'one1two22three333four4444five5six6'
#one@two@three@four@five@six@

p = re.compile(r"\d+")
rest = p.sub('@',s)
print(rest)

#使用正则表达式更换位置
s2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)')
rest_pos = p2.sub(r"\2 \1",s2)
print(rest_pos)

#在原有的基础上，替换并改变内容
def f(m):
    '''使用函数进行替换规则改变'''
    return m.group(1).upper() + ' ' + m.group(2)


rest_change = p2.sub(f,s2)
print(rest_change)

#使用匿名函数进行替换改变 lambda
rest_lamb = p2.sub(lambda m:m.group(2).upper() + ' ' + m.group(1), s2)
print('----------')
print(rest_lamb)