def pow_number(l):
    '''
    根据给定的列表数据，计算每一个项目的立方
    :param l: 给定一个list/tuple int类型的
    :return: 原来列表中的每一项的立方
    '''
    rest_list = []
    for x in l:
        rest_list.append(x ** 3)
    return  rest_list

def pow_use_map(l):
    '''
    使用map（）函数计算列表的每一项的立方
    :param l: list/tuple inte类型
    :return: 原来列表中的每一项的立方
    '''
    rest = map(lambda n: n ** n,l)
    return rest

if __name__ == '__main__':
    l = [1 , 2, 3, 4, 5, 6, 7, 8, 9]
    rest =  pow_number(l)
    print(rest)
    rest2 = pow_use_map(l)
    print(list(rest2))