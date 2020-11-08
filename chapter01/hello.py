'''
文档注释
这是hello模块，我们自己定义的模块
'''
SYS_DATE = 'ABC123'


def func():
    '''
    定义一个hello函数
    '''
    print("hello，imooc")

def add(num1,num2):
    '''
    注释模板
    这是一个加法函数
    :param num1: 第一个数
    :param num2: 第一个数
    :return: 第一个数和第二个数的和
    '''
    #1.xxxx伪代码

    #2.xxxx
    return num1 + num2

if __name__ == '__main__':
    func()