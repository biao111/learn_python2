from functools import reduce


def get_sum(l):
    '''
    根据给定的列表，求里面各个数字的总和
    :param l: list/type int
    :return: sum
    '''
    rest = 0
    for i in l:
        rest += i
    return rest

def get_sum_py(l):
    '''
    python内置的求和方法
    :param l:
    :return:
    '''
    return sum(l)
def f(m,n):
    '''两个数求和 '''
    return m + n

def use_reduce(l):
    '''
    使用reduce进行求和
    :param l:
    :return:
    '''
    return reduce(f,l)

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    rest1 = get_sum(l)
    print(rest1)
    print("...........")
    rest2 = get_sum_py(l)
    print(rest2)
    print('........')
    rest3 = use_reduce(l)
    print(rest3)