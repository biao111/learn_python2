'''
猫科动物的细化
            猫科动物类BaseCat
        /        |          \
    Tiger类    Panda类      PetCat类
                            /       \
                    Duancat 类    HuaCat 类
'''

class BaseCat(object):
    '''
    猫科动物的基础类
    '''
    tag = '猫科动物'

    def __init__(self,name):
        print('BaseCat init')
        self.name = name

    def eat(self):
        '''猫吃东西'''
        print('猫都吃东西')



class Tiger(BaseCat):
    '''
    老虎类也是猫科动物
    '''

    def __init__(self,name,color):
        print('Tiger init')
        super().__init__(name)
        self.color = color     #皮毛的颜色

    def eat(self):
        # #调用父类方法
        # super().eat()
        '''重写、重载'''
        print('我还喜欢吃肉，大猪肉')

    def show_info(self):
        '''展示信息'''
        print('Tiger: {0},颜色： {1}'.format(self.name,self.color))



class Panda(BaseCat):
    '''
    熊猫类也是猫科动物
    '''
    pass


class PetCat(BaseCat):
    '''
    家猫类
    '''
    def eat(self):
        super(PetCat, self).eat()
        print('我还喜欢吃猫粮')


class HuaCat(PetCat):
    '''
     中华田园猫
    '''
    def eat(self):
        super(HuaCat, self).eat()
        print('我还喜欢吃零食')



class DuanCat(PetCat):
    '''
     英短
    '''
    def eat(self):
        print('我啥都吃')

if __name__ == '__main__':

    tiger = Tiger('华南虎','黄色')
    tiger.show_info()