

class MyException(Exception):
    '''自定义异常类'''
    pass

def v_for():
    ''' 自定义函数 '''
    for i in range(1,100):
        if i ==20:
            raise MyException
        print(i)

def call_v_for():
    ''' 调用v_for函数 '''
    print('开始调用v_for')
    v_for()
    print('结束调用函数')

def test_raise():
    print('测试函数')
    call_v_for()
    print('测试结束')

if __name__ == '__main__':
    test_raise()