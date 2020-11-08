

class ApiException(Exception):
    '''我的自定义异常'''
    err_code = ''
    err_msg = ''

    def __init__(self, err_code=None, err_msg=None):
        '''
        自定义err_cord,err_msg
        :param err_code: 错误代码
        :param err_msg:错误码描写
        '''
        self.err_code = self.err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg

    def __str__(self):
        return 'Error:{0}-{1}'.format(self.err_code, self.err_msg)

class InvalidCtrlExec(ApiException):
    '''
    当参数不合法时触发
    40001	invalid credential	不合法的调用凭证
    '''
    err_code = '40001'
    err_msg = '不合法的调用凭证'

class BadPramsException(ApiException):
    '''参数不正确'''
    err_code = '40002'
    err_msg = '两个参数必须是整数'

def divide(num1,num2):
    '''除法的实现'''
    #两个数必须为整数
    if not isinstance(num1,int) or not isinstance(num2,int):
        raise BadPramsException('40000','两个参数必须都是整数')
    #除数不能为0
    if num2 == 0:
        raise ApiException('40000','除数不能为0')
    return num1 / num2

if __name__ == '__main__':
    try:
        rest = divide(5,'s')
        print(rest)
    #先抓子类在抓父类
    except BadPramsException as e:     #子类
        print('---------')
        print(e)
    except ApiException as err:         #父类
        print('出错了')
        print(err)
