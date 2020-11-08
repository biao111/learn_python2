import pymongo

Myclient = pymongo.MongoClient("mongodb://10.12.193.215:27017")

mydb = Myclient["imooc"]
mycollection = mydb["pymongo_test"]

# mycollection.insert_one({"name":"imooc","flag":1,"url":"https://www.imooc.com"})
# result = mycollection.insert_one({"name":"baidu","flag":2,"url":"https://www.baidu.com"})
# print(result)
# mylist = [
#     {"name":"taobao","flag":100,"url":"https://www.taobao.com"},
#     {"name":"qq","flag":101,"url":"http://www.qq.com"},
#     {"name":"facebook","flag":102,"url":"https://www.facebook.com"},
#     {"name":"知乎","flag":103,"url":"https://www.zhihu.com"},
#     {"name":"Github","flag":104,"url":"https://www.github.com"}
# ]
# result = mycollection.insert_many(mylist)
# print(result)
# result = mycollection.find()
# for item in result:
#     print(item)
#result = mycollection.find({},{'_id':0,"name":1,"flag":1})
#mycollection.update_one({"name":{"$regex":"G"}},{"$set":{"name":"jd"}})
#mycollection.delete_one({"url":"https://www.imooc.com"})
mycollection.delete_many({"url":{"$regex":"https?://www\.[tq]"}})
for item in mycollection.find():
    print(item)

