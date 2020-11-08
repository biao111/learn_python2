from db.type_dao import TypeDao

class TypeService:
    __type_Dao = TypeDao()

    # 查询新闻类型列表
    def search_list(self):
        result = self.__type_Dao.search_list()
        return result