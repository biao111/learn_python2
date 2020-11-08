import sys

i = 1

l = []
l2 = l
l3 = l

l5 = l3
print(sys.getrefcount(l))

del l2
print(sys.getrefcount(l))

#对象l被引用的数量
print(sys.getrefcount(l))

print('--------------------')
print(sys.getrefcount(i))
a = i
print(sys.getrefcount(i))