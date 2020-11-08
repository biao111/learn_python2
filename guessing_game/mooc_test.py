
import random
import sys
from datetime import datetime

'''记录要输入标题的文字'''
def guide_page(guide_word):
    '''拼接“*“号和标题文字信息'''
    print('************{}***********'.format(guide_word))

def all_num(n):
    """判定指定的值是否为数字"""
    return n.isdigit()

def num_lengal(ls):
    '''取出列表中的值进行比较'''
    #若二者相等
    if int(ls[0]) == int(ls[1]):
        #提示玩家重新启动程序
        print("请您输入区间数字相同！请重新启动程序。")
        #退出程序
        sys.exit()
    #若数字的起始数字大于终止位置的值
    elif int(ls[0]) > int(ls[1]):
        # 提示玩家重新启动程序
        print("请您输入区间数字大小有误！请重新启动程序。")
        # 退出程序
        sys.exit()
    else:
        return 1


def set_final_num(num1,num2):
    '''根据参数值产生一个位于参数值区间内的随机数'''
    #将两个参数保存在列表中
    ls = [num1,num2]
    #过滤确保全部为数字
    ls = list(filter(all_num, ls))
    #判断全部是否位数字
    if len(ls) == 2:
        #调用自定义的等值判断函数
        if num_lengal(ls) == 1:
            #返回区间内的随机数
            return random.randint(int(num1),int(num2))
    #否则输入非法值
    else:
        print("您输入了非数字字符，请重新启动")
        sys.exit()

def check_num_legal(num):
    '''判断所输入的值是否在指定区间内'''
    if num < int(i) or num > int(j):
        print('您输入的数字未在指定区间内')
        return True
    else:
        return False

def write_record(times,value):
    #将获取的参数和时间信息 用追加的方式写入日志文件
    with open('record.txt','a+',encoding='utf-8') as f:
        #根据datetime模块获取玩家没测猜测的时间
        f.write('{d}:第{t}次您猜测数字为：{v}\n'.format(d = datetime.now(),t = times, v = value))

def main(rand1):
    '''主函数'''
    #temp接受随机数
    temp = rand1
    #记录猜测的次数
    times = 0
    #无限循环
    while True:
        num = int(input("请您要输入猜测的数字："))
        print('**********')
        if check_num_legal(num):#核查函数值，如果为真，则跳过本次循环
            continue
        #判断用户猜测的数字是否=，<,>
        if num == temp:
            times += 1
            write_record(times,num)#调用日志函数，传入猜测的次数和用户猜测的数字
            print('恭喜您，用了{}次赢得了游戏'.format(times))
            break
        elif num > temp:
            times += 1
            write_record(times,num)
            print('Hight than answer')
        else:
            times += 1
            write_record(times, num)
            print('lower than answer')

if __name__ == '__main__':
    #调用guide_page()输出效果图的标志信息
    guide_page("欢迎进入数字猜猜猜小游戏")
    #设置两个变量为i，j分别按照输入数字区间的起始值和终止值
    i = input('数字的起始值')
    j = input('数字的终止值')
    #调用rand1 = set_final_num()函数得到的随机数
    rand1 = set_final_num(num1 = i ,num2 = j)
    #调用main（）函数执行
    main(rand1)