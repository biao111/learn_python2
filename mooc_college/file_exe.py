from example import Teacher,Student,Course

def introduction(str):
    ''' 标题 函数 '''
    a = '*' * 22
    print('{0}{1}{2}'.format(a,str,a))

def prepare_course():
    ''' 创建课程信息初始化 '''
    #（1）创建字典接收课程信息
    dict1 = {
              "01": "网络爬虫", "02": "数据分析",
              "03": "人工智能", "04": "机器学习",
              "05": "云计算",   "06": "大数据",
              "07": "图像识别", "08": "Web开发"
              }
    #（2）创建空列表
    list1 = []
    #（3）循环遍历字典中的数据，将课程编号和课程姓名传入课程类得到课程类的实例，空列表追加每一次的课程类实例
    for k,v in dict1.items():
        rest = Course(k,v)
        list1.append(rest)
    #（4）返回追加后的列表
    return list1

def create_teacher():
   ''' 创建教师信息初始化 '''
   #1. 列表保存教师信息
   list_t = ["T1", "张亮", "13301122001"],["T2", "王朋", "13301122002"],\
            ["T3", "李旭", "13301122003"],["T4", "黄国发", "13301122004"],\
            ["T5", "周勤", "13301122005"],["T6", "谢富顺", "13301122006"],\
            ["T7", "贾教师", "13301122007"],["T8", "杨教师", "13301122008"]
   #2. 创建列表进行存储
   list2 = []
   #3.将8个教职信息传入
   for i in list_t:
       rest = Teacher(i[0],i[1],i[2])
       list2.append(rest)
    #4. 返回教职信息
   return list2

def course_to_teacher():
    ''' 课程与教师逐一绑定，每一个课程信息绑定每一个教师信息 '''
    list3 = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    for i in range(0,len(ls_course)):
        rest = ls_course[i].binding(ls_teacher[-(i+1)])
        list3.append(rest)
    return list3

def create_student():
    ''' 创建学生信息初始化 '''
    #1. 列表保存学生信息
    ls_student = [ "小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    #2. 学号列表
    ls_s_num = list(range(1000,1008))
    #3. 创建空列表
    list4 = []
    #4. 循环遍历学生信息的长度，将学号与（据效果图所示）倒叙的学生姓名传入学生类，得到学生类的实例，将学生类实例追加至空列表
    for i in range(0,len(ls_student)):
        rest = Student(ls_s_num[i],ls_student[-(i+1)])
        list4.append(rest)
    return list4

if __name__ == '__main__':
    rest1 = course_to_teacher()
    rest2 = create_student()
    introduction("慕课学院(1)班学生信息")
    for i in rest2:
        print(i)
    introduction("慕课学院(1)班选课信息")
    #调用学生类中的函数添加课程
    for i in range(0,len(rest1)):
        rest2[i].add_course(rest1[i])
    for j in rest2:
        print('Name:{0},Select{1}'.format(j.s_name,j.course_detail))