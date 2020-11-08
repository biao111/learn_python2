from datetime import datetime

from trans import tools as trans_tools
#from work import tools as work_tools
import work

def test_trans_tools():
    ''' 测试trans包下的tools模块'''
    id1 = trans_tools.gen_trans_id()
    print(id1)
    date = datetime(2015, 10, 2, 12, 30, 45)
    id2 = trans_tools.gen_trans_id(date)
    print(id2)

def test_work_tools():
    ''' 测试work模块'''
    file_name = 'C:\\Users\\yubiao\\Desktop\\操作系统\\ppt\\0课程概述.ppt'
    rest = work.tools.get_file_type(file_name)
    print(rest)

if __name__ == "__main__":
    test_trans_tools()
    test_work_tools()