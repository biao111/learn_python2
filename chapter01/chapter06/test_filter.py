"""

  def f(n):
     判断给定的数是不是奇数
    return n % 2 != 0
"""

def use_filer(l):
    """
    获取指定元组/列表中的奇数
    :param l :list/tuple 要过滤的数据
    :return: 过滤好的奇数列表
    """
    #filer()是给一个元组，在给定一个条件过滤掉
    rest = filter(lambda n: n % 2 != 0,l)#lambda匿名的函数，表达式，返回的是布尔值
    #rest = filter(f,l)
    return rest


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    rest = use_filer(l)
    print(list(rest))