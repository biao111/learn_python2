import os
import os.path

class FileBackup(object):
    '''
    文本文件备份
    '''

    def __init__(self,src,dist):
        '''
        构造方法
        :param src:目录 需要备份的目录
        :param dist: 目录 备份后的目录
        '''
        self.src = src
        self.dist = dist


    def read_files(self):
        '''
        读取src目录下的所有文件
        '''
        ls = os.listdir(self.src)
        print(ls)
        for l in ls:
            #循环处理每一个文件/文件夹
            #self.back_up(l)
            self.back_up2(l)

    def back_up2(self, file_name):
        '''文件备份-优化版'''
        # 1.判断dist是否存在，如果不存在，则创建这个目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定的文件不存在，创建完成")

        # 2.判断文件为是否我们想要的文件
        # 拼接完整的路径
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)

        # 首先要判断是否为文件夹，然后可以借助于文件的后缀名进行判断
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            # 3.读取文件内容
            with open(full_dist_path, 'w', encoding='utf-8') as f_dist,\
                open(full_src_path, 'r', encoding='utf-8') as f_src:
                print('>>开始备份【{0}】'.format(file_name))
                while True:
                    rest = f_src.read(100)
                    if not rest:
                        break

                    # 4.把读取到的内容写入新的文件中
                    f_dist.write(rest)
                f_dist.flush()  # 将剩余部分全部写进去
        else:
            print("文件类型不符合备份要求。跳过>>")
            print('>>【{0}】备份完成'.format(file_name))

    def back_up(self,file_name):
        '''文件备份'''
        # 1.判断dist是否存在，如果不存在，则创建这个目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定的文件不存在，创建完成")

        # 2.判断文件为是否我们想要的文件
        #拼接完整的路径
        full_src_path = os.path.join(self.src,file_name)
        full_dist_path = os.path.join(self.dist,file_name)

        # 首先要判断是否为文件夹，然后可以借助于文件的后缀名进行判断
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            print(full_src_path)
            # 3.读取文件内容
            with open(full_dist_path,'w',encoding='utf-8') as f_dist:
                print('>>开始备份【{0}】'.format(file_name))
                with open(full_src_path,'r',encoding='utf-8') as f_src:
                    while True:
                        rest = f_src.read(100)
                        if not rest:
                            break

                        # 4.把读取到的内容写入新的文件中
                        f_dist.write(rest)
                    f_dist.flush()                                      #将剩余部分全部写进去
        else:
            print("文件类型不符合备份要求。跳过>>")
            print('>>【{0}】备份完成'.format(file_name))

if __name__ == '__main__':
    # #要备份文件的目录地址
    # src_path = 'D:\\Code\\Python\\chapter04\\src'
    # #备份后文件的地址
    # dist_path = 'D:\\Code\\Python\\chapter04\\dist'

    #当前代码的目录名称
    #D:\\Code\\Python\\chapter04\\test_back_up.py
    base_path = os.path.dirname(os.path.abspath(__file__))
    #要备份文件的目录地址
    src_path = os.path.join(base_path,'src')
    print(src_path)
    #备份后文件的地址
    #dist_path = 'D:\\Code\\Python\\chapter04\\dist'
    dist_path = os.path.join(base_path, 'dist')
    print(dist_path)
    bak = FileBackup(src_path,dist_path)
    bak.read_files()