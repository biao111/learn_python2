

def f(self):
    print('{0}>我要吃东西'.format(self.name))

def eat(cls):
   # cls.eat = lambda self: print('{0}>我要吃东西'.format(self.name))
    cls.eat = f
    return cls
@eat
class Cat(object):
    '''猫类'''
    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    cat = Cat('小黑')
    cat.eat()