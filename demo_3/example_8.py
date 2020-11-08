from mongo_db import client
from bson.objectid import ObjectId
from gridfs import GridFS

db = client.school
gfs = GridFS(db,collection="book")

try:
    document = gfs.get(ObjectId("5f2f8430fffa1c3d1279d0dc"))
    file = open("D:/第san讲.pdf","wb")
    file.write(document.read())
    file.close()
except Exception as e:
    print(e)