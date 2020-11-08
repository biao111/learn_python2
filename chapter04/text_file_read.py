
def read_file():
    ''' 读取文件'''
    #使用相对路径
    file_name = 'test.txt'
    #使用绝对路径
    file_path  = 'D:\\Code\\Python\\chapter04\\test.txt'
    file_path2 = 'D:/Code/Python/chapter04/test.txt'

    #使用with打开文件
    with open(file_name,encoding='gbk') as f:
    # 使用普通的方式打开
    #f = open(file_name,encoding='gbk')
        #读取文件所有的内容
        #rest = f.read()
        #print(rest)
        #读取指定的内容
        #rest = f.read(8)
        #print(rest)

        #随机读取：跳过指定的数后，然后读取字符
        #f.seek(20)
        #print(f.read(5))
        #按行读取
        rest = f.readline()
        print(rest)
        print(f.readline())
        print(f.readline())
        #关闭文件
        #f.close()
if __name__ == '__main__':
    read_file()