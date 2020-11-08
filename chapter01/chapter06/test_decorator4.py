from functools import wraps


def log(name = None):                               # 装饰器的参数
    '''记录函数执行的日志'''

    def decorator(func):                            # 传入函数
        
        @wraps(func)
        def wrapper(*args ,**kwargs):               # 带参函数需要传入*args,**kwargs
            '''装饰器内部函数'''
            print('{0}开始执行'.format(name))
            rest =func(*args, **kwargs)             # 带参的函数需要将返回值临时保存起来
            print('{0}结束执行'.format(name))
            # warpper.__doc__ = func.__doc__
            # warpper.__name__ = func.__name__      #等于@wraps
        return wrapper

    return decorator


# 函数不带参
@log('hello')
def hello():
    '''简单功能模拟'''
    print('hello world')

if __name__ == "__main__":
    print('doc:{0}'.format(hello.__doc__))
    print('name:{0}'.format(hello.__name__))
    hello()