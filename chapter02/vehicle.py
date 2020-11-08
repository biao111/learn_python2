

class Vehicle(object):
    '''交通工具类'''

    def __init__(self,speed,size,trans_type = 'SUV'):
        self.__speed = speed
        self.size = size
        self.trans_type = trans_type

    def show_info(self):
        #打印所属类型的速度和体积的值
        info = '该交通工具的类型：{t}，速度{sp}km/h，体积{si}m'.format(t = self.trans_type,sp = self.__speed,si = self.size)
        print(info)
        return info

    def move(self):
        '''
        前进五十米
        '''
        print('我一向前移动了五十米')

    def set_speed(self,new_speed):
        '''
        修改speed
        :param new_speed: int speed
        :return: 更改后的速度
        '''
        self.__speed = new_speed
        return self.__speed

    def get_speed(self):
        '''打印设置的速度'''
        print('我的时速为{0}'.format(self.__speed))

    def speed_up(self):
        '''实例加速'''
        speed_up = self.__speed + 10
        print('我的速度由{set}km/h上升到了{up}km/h'.format(set = self.__speed,up = speed_up))

    def speed_down(self):
        '''实例降速'''
        speed_down = self.__speed - 15
        print('我的速度由{set}km/h下降到了{down}km/h'.format(set = self.__speed,down = speed_down))

    def transport_identify(self):
        '''判断vehicle的类型'''
        if isinstance(car,Vehicle) is True:
            print('匹配成功')
        else:
            print('匹配不成功')

if __name__ == '__main__':
    '''实例交通工具'''
    car = Vehicle(20,(3.6,1.9,1.75))
    car.show_info()
    car.move()
    car.set_speed(40)
    car.get_speed()
    car.speed_up()
    car.speed_down()
    car.transport_identify()