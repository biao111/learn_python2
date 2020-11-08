

class Cat(object):
    '''家猫类'''
    def __init__(self,name,age):
        '''
        构造方法
        :param name:猫的名称
        :param age: 年龄
        '''
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if not isinstance(value,int):
            print("年龄只能整数")
            return 0
        if value < 0 or value > 100:
            print('年龄只介于0——100之间')
            return 0
        self.__age = value

    #描述符
    @property
    def show_info(self):
        '''显示猫的信息'''
        return '我叫{0}，今年{1}岁'.format(self.name,self.age)

    #方便调试时，把类的描述打印出来
    def __str__(self):
        return '我的对象：{0}'.format(self.name)


if __name__ == '__main__':
    cat_black = Cat('小黑',2)
    rest = cat_black.show_info
    print(rest)
    #改变年龄
    cat_black.age = 'bbbb'
    rest = cat_black.show_info
    print(rest)
    #print(cat_black)
