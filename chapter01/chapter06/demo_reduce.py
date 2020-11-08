from functools import reduce


def use_reduce(l):
    result = reduce(lambda  m, n : m * n, l)
    return  result

if __name__ == '__main__':
    data = list(range(1,21))
    rest1 = use_reduce(data)
    print(rest1)