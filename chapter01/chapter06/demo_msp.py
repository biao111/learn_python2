
def use_map(data):
    '''
    求元组的各个元素的5次方
    :param data: tuple
    :return: 过滤好的元组的各个元素的5次方
    '''
    result = map(lambda  n:pow(n,5),data)
    return result

if __name__ == '__main__':
    data = (2, 4, 6, 8, 10, 12)
    result = use_map(data)
    print(tuple(result))