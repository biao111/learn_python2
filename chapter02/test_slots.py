

class Cat(object):
    '''家猫类'''
    __slots__ = ('name','__age')

    def __init__(self,name,age):
        '''
        构造方法
        :param name:猫的名称
        :param age: 年龄
        '''
        self.name = name
        self.__age = age


    #描述符
    @property
    def show_info(self):
        '''显示猫的信息'''
        return '我叫{0}，今年{1}岁'.format(self.name,self.__age)

    #方便调试时，把类的描述打印出来
    def __str__(self):
        return '我的对象：{0}'.format(self.name)


class HuaCat(Cat):
    '''中华田园猫'''
    pass


def eat():
    print('我喜欢吃鱼')




if __name__ == '__main__':
    # cat_black = Cat('小黑',2)
    # rest = cat_black.show_info
    # print(rest)
    # 使用slots后不能允许添加新的属性、方法、函数#给实例添加新的属性
    # cat_black.color = '白色'
    # print(cat_black.color)
    # #给实例添加新的方法
    # cat_black.eat = eat
    # cat_black.eat()
    cat_white = HuaCat('小白',3)
    rest = cat_white.show_info
    print(rest)
    #父类的__slots__在子类不生效
    cat_white.color = '白色'
    print(cat_white.color)