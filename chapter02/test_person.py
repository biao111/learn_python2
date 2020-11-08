

class Person(object):
    '''人类'''
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print('hello，我是{0}'.format(self.name))


class Student(Person):
    '''学生类'''
    def __init__(self,name,gender,score,major,__num = '2018014002'):
        super(Student, self).__init__(name,gender)
        self.score = score
        self.major = major
        self.__num = __num

    def speak(self):
        super(Student, self).speak()
        print("我的学号为：{0},很高兴认识大家".format(self.__num))

    def identify_stu(self):
        if '2018014002' in self.__num:
            print('我的分组已完成')
        else:
            print('请稍后，马上为你自动分组')

    def set_num(self,new_num):
        '''将学号重写设置'''
        self.__num = new_num

    def relation(self):
        '''判断Student类是否为为Person类的子类'''
        if issubclass(Student,Person) is True:
            print("我的父类是person")
        else:
            print('父类正在查询中.....')


if __name__ == '__main__':
    stu = Student('小明','男',99,'math')
    stu.speak()
    stu.identify_stu()
    stu.relation()
    print("-------------")
    stu2 = Student('小红','女',99,'math')
    stu2.set_num('2018040625')
    stu2.speak()
    stu2.identify_stu()
    stu2.relation()