from db.mongo_db import client
from bson.objectid import ObjectId

class MongoNewsDao:
    #添加新闻正文记录
    def insert(self,title,content):
        try:
            client.vega.news.insert_one({"title":title,"content":content})
        except Exception as e:
            print(e)

    #查询新闻正文主键值
    def search_id(self,title):
        try:
            news = client.vega.news.find_one({"title":title})
            return str(news["_id"])
        except Exception as e:
            print(e)

    #修改新闻的标题和正文
    def update(self,id,title,content):
        try:
            client.vega.news.update_one({"_id":ObjectId(id)},
                                    {"$set":{"title":title,"content":content}})
        except Exception as e:
            print(e)

    #查询新闻的正文（通过mongodb的_id查询）
    def conetent_by_id(self,id):
        try:
            news = client.vega.news.find_one({"_id":ObjectId(id)})
            return news["content"]
        except Exception as e:
            print(e)

    #删除新闻
    def delete_by_id(self,id):
        try:
            client.vega.news.delete_one({"_id":ObjectId(id)})
        except Exception as e:
            print(e)