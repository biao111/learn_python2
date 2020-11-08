

def use_ranger():
    '''python内置函数range函数'''
    for i in range(5,10):
        print(i)

#用迭代器模拟range（）
class IterRange(object):
    ''' 使用迭代器模拟range'''

    def __init__(self,start,end):
             self.start = start -1
             self.end = end

    def __next__(self):
         self.start += 1
         if self.start >= self.end:
             raise StopIteration
         return self.start

    def __iter__(self):
         return self

#用生成器模拟range
class GenRange():
    '''使用生成器模拟range'''

    def __init__(self,start,end):
             self.start = start -1
             self.end = end

    def get_num(self):
        while True:
            if self.start >= self.end - 1:
                break
            self.start += 1
            yield self.start

def get_num(start,end):
    start -= 1
    while True:
        if start >= end - 1:
            break
        start += 1
        yield start

if __name__ == '__main__':
    use_ranger()
    print('----------')
    iter = IterRange(5,10)
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    l = list(iter)
    print(l)
    print('--------')
    gen = GenRange(5,10).get_num()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    print(list(gen))
    print('---------')
    gen_f = get_num(5,10)
    print(gen_f)
    print(list(gen_f))