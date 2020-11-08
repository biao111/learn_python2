from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId

db = client.school
gfs = GridFS(db,collection="book")

try:
    gfs.delete(ObjectId("5f2f8430fffa1c3d1279d0dc"))

except Exception as e:
    print(e)