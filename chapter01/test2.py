import random

#import django

import pay

from pay.alipay.tools import pay as ali_pay
from pay.wechat_pay.tools import pay as we_pay
#import顺序
#1.标准库 2.第三方库包 3.自定义的包/模块

#PEP8规范
def funct():
    '''局部引入'''
    import pay

def func2():
    pass
     #tools.pay()

def func3():
    ali_pay()
    we_pay()

if __name__ == "__main__":
    func2()