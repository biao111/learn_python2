
class Cat(object):
    '''猫科动物类'''
    tag = '猫科动物类'

    def __init__(self,name,age):
        self.name = name
        self.__age =age

    def catch(self):
        print('猫可以抓老鼠。')

    def eat(self):
        print('猫喜欢吃鱼')

    def get_age(self):
        print("{0}的年龄是{1}岁".format(self.name,self.__age))
