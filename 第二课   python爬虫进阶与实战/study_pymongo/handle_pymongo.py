import pymongo

#pymongo.MongoClient,mongodb://192.168.110.129:27017
myclient = pymongo.MongoClient("mongodb://192.168.110.129:27017")
#当前指定的数据库的名称imooc
#如果没有插入数据，库和表都不会创建
mydb = myclient['imooc']
mycollection = mydb['pymongo_test']
#表.insert_one插入一条记录
# mycollection.insert_one({"name":"imooc","flag":1,"url":"https://www.imooc.com"})
#insert_one这个方法，返回了一个InsertOneResult对象
# result = mycollection.insert_one({"name":"baidu","flag":2,"url":"https://www.baidu.com"})
# print(result)
# mylist = [
#     {"name":"taobao","flag":100,"url":"https://www.taobao.com"},
#     {"name":"qq","flag":101,"url":"http://www.qq.com"},
#     {"name":"facebook","flag":102,"url":"https://www.facebook.com"},
#     {"name":"知乎","flag":103,"url":"https://www.zhihu.com"},
#     {"name":"Github","flag":104,"url":"https://www.giuhub.com"}
# ]
#
# #插入多条数据，返回了InsertManyResult对象
# result = mycollection.insert_many(mylist)
# print(result)
#通过find方法，返回了一个游标数据cursor.Cursor
# result = mycollection.find()
# for item in result:
#     print(item)

#在find方法里，加上限定条件，前面大括号,查询所有，后面的大括号代表限定条件
#0代表不显示，1代表显示
# result = mycollection.find({},{'_id':0,"name":1,"flag":1})
# for item in result:
#     print(item)

#通过find_one方法来查看第一条数据，可以做为示例数据,他的返回就是数据，而不是游标
# result = mycollection.find_one()
# print(result)
#find方法可以嵌套一些高级查询，大于$gt$lt
# result = mycollection.find({"flag":{"$gt":100}})
# for item in result:
#     print(item)

#find方法可以嵌套进正则表达式
# result = mycollection.find({"name":{"$regex":"^G"}})
# for item in result:
#     print(item)

#通过update_one来更新数据，有两个参数，第一个参数是查询条件，第二个参数要改成什么样
#update_one只改第一条
# mycollection.update_one({"name":{"$regex":"^G"}},{"$set":{"name":"jd"}})
# result = mycollection.find()
# for item in result:
#     print(item)

#通过uodate_many来更改多条数据
# mycollection.update_many({},{"$set":{"name":"imooc"}})
# for item in mycollection.find():
#     print(item)

# #delete_one是删除一条数据
# mycollection.delete_one({"url":"https://www.imooc.com"})
# for item in mycollection.find():
#     print(item)

#通过delete_many删除多条数据
# mycollection.delete_many({"url":{"$regex":"https?://www\.[tq]"}})
#通过delete_many来删除所有数据，{}代表所有数据
# mycollection.delete_many({})
# for item in mycollection.find():
#     print(item)





