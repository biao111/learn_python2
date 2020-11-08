

def hello():
    '''简单功能模拟'''
    print('hello world')

def hello_wrapper():
    '''包裹原来的函数'''
    print('开始执行hello')
    hello()
    print('结束执行hello')

if __name__ == '__main__':
    hello()
    hello_wrapper()