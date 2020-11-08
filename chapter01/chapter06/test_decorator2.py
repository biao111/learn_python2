

def log(func):
    '''记录函数执行的日志'''

    def wrapper():
        print('开始执行')
        func()
        print('结束执行')
    return wrapper

@log #装饰器
def hello():
    '''简单功能模拟'''
    print('hello world')

if __name__ =='__main__':
    hello()