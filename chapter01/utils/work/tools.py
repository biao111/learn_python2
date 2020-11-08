import os.path

import constants


def get_file_type(file_name):
    """
    根据文件的名称，判断文件的类型
    :param file_name: str 文件的名称
    :return: int 文件的类型
    -1.未知类型的文档
    0.图片类型的文档
    1.word类型的文档
    2.excle类型的文档
    3.ppt文档
    """
    #默认文件是未知类型
    result = constants.FILE_TYPE_UNKNOW
    #传进来的必须是一个文件的名称
    if not os.path.isfile(file_name):
        return  result
    path_name, ext = os.path.splitext(file_name)
    #将文件名的后缀名统一成小写
    ext = ext.lower()
    #图片类型
    if ext in ('.png','.jpg','.gif','.bmp'):
        result = constants.FILE_TYPE_IMG
        return result
    #文件类型
    elif ext in ('.doc','docx'):
        result = constants.FILE_TYPE_DOC
        return result
    #表格类型
    elif ext in ('.xls','.xlsx'):
        result = constants.FILE_TYPE_EXCLE
        return result
    #ppt类型
    elif ext in ('.ppt','pptx'):
        result = constants.FILE_TYPE_PPT
        return result