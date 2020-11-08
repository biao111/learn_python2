

class Cat(object):

    @staticmethod
    def breath():
        '''呼吸'''
        print('猫都需要呼吸')

if __name__ == '__main__':
    #通过类的调用
    Cat.breath()
    #通过类的实例调用 
    cat = Cat()
    cat.breath()