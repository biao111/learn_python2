

def log(name = None):                           #装饰器的参数
    '''记录函数执行的日志'''

    def decorator(func):                        #传入函数

        def wrapper(*args,**kwargs):            #带参函数需要传入*args,**kwargs
            print('{0}开始执行'.format(name))
            print(args)
            print(kwargs)
            rest =func(*args,**kwargs)          #带参的函数需要将返回值临时保存起来
            print('{0}结束执行'.format(name))
            return rest                         #返回函数返回值
        return wrapper
    return decorator

 #函数不带参
@log('hello')
def hello():
    '''简单功能模拟'''
    print('hello world')

#函数带参
@log('add函数')
def add(a,b,*args,**kwargs):
    return a + b

if __name__ =="__main__":
   # hello()

    rest = add(5,6,k = 5,v = 6)
    print(rest)