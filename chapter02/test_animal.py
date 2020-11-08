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
        self.name = name

    def eat(self):
        '''猫吃东西'''
        print('猫都吃东西')


class ProtectedMixin(object):
    '''受保护的动物'''

    def protected(self):
        print('我是受保护的动物')

 #基类下的属性、方法重名，调用第一个，容易产生bug
class CountryProtectedMixin(object):
    '''受保护的动物'''

    def protected(self):
        print('我是受保护的动物')

class Tiger(BaseCat,ProtectedMixin):
    '''
    老虎类也是猫科动物
    '''
    def eat(self):
        # #调用父类方法
        # super(Tiger, self).eat()
        '''重写、重载'''
        print('我还喜欢吃肉，大猪肉')


class Panda(BaseCat,ProtectedMixin):
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
    # #实例化中华田园猫
    # cat = HuaCat('小黄')
    # cat.eat()
    # print('--------------')
    # #实例化短毛猫
    # cat_d = DuanCat('小辉')
    # cat_d.eat()
    # print('--------------')
    # #子类的判断
    # print(issubclass(DuanCat,BaseCat))

    panda = Panda('卧龙大熊猫')
    panda.eat()
    panda.protected()

    tiger = Tiger('华南虎')
    tiger.protected()
    print("--------")
    '''验证信息'''
    print(issubclass(Panda,BaseCat))
    print(issubclass(Panda,ProtectedMixin))