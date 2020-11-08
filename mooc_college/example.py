

class Student(object):
    ''' 学生类 '''
    def __init__(self,s_num,s_name):
        '''

        :param s_num: 学生学号
        :param s_name: 学生姓名
        :param s_course：学生已选的课程，默认空列表
        '''
        self.s_num = s_num
        self.s_name = s_name
        self.s_course = []

    @property
    def course_detail(self):
        '''设定course_detail方法以属性的方式返回学生的已选课程信息'''
        return self.s_course

    def add_course(self,cour_info):
        ''' 实现添加课程信息至学生对象的已选课程属性 '''
        self.s_course.append(cour_info)

    def __str__(self):
        ''' 设置学生信息的字符串显示方法'''
        return 'name:{0},s_number:{1}'.format(self.s_name,self.s_num)


class Teacher(object):
    ''' 教师类 '''
    def __init__(self,t_num,t_name,t_phone):
        '''

        :param t_num: 教师编号
        :param t_name: 教师姓名
        :param t_phone: 教师手机号
        '''
        self.t_num = t_num
        self.t_name = t_name
        self.t_phone = t_phone

    def __str__(self):
        ''' 设置教师信息的字符串显示方法'''
        return 't_number:{0},name:{1}'.format(self.t_num,self.t_name)


class Course(object):
    ''' 课程类 '''
    def __init__(self,c_num,c_name,c_teacher = None):
        '''

        :param c_num: 课程编号
        :param c_name: 课程名称
        :param c_teacher: 授课教师，默认为空
        '''
        self.c_num = c_num
        self.c_name = c_name
        self.c_teacher = c_teacher

    def binding(self,teacher):
        ''' 绑定授课教师'''
        #判断
        #1.实力不存在，返回0
        #2.存在，将该实例赋值给课程类的授课教师属性
        #       并将课程名称和教师名称包装成字典进行返回
        if teacher == '':
            return 0
        else:
            self.c_teacher = teacher
            return {'课程名称':self.c_name,'教师名称':self.c_teacher.t_name}