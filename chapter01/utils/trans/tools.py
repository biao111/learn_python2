import random
from datetime import datetime


def gen_trans_id(date = None):
     '''
     根据传入的时间得到一个唯一的交易流水id
     :param date: 日期
     :return: 交易流水id字符串
     '''
     #如果没有传入时间，则使用系统的当前时间
     if date is None:
         date = datetime.now()
     #怎样保证字符串的唯一
     #日期+时间+随机数（6位随机数）
     return '{0}{1}'.format(date.strftime('%Y%m%d%H%M%S%f'),random.randint(10000,999999))
     #return date.strftime('%Y%m%d%H%M%S%f') + str(random.randint(10000,999999))