from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId
import math
import datetime

db = client.school
gfs=GridFS(db,collection="book")
book = gfs.find_one({"filename":"第二讲.pdf"})
print(book.filename)
print(book.type)
print(book.keyword)
print("%dM"%math.ceil(book.length/1024/1024))
print("-------------")
books = gfs.find({"type":"PDF"})
for one in books:
    uploadDate = one.uploadDate + datetime.timedelta(hours=8)
    #格式化日期
    uploadDate = uploadDate.strftime("%Y-%m-%d %H:%M:%S")
    print(one._id,one.filename,one.uploadDate)
print("-------------")
rs = gfs.exists(ObjectId("5f2f8430fffa1c3d1279d0dc"))
print(rs)
rs = gfs.exists(**{"filename":"123.html"})
print(rs)