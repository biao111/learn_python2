from mongo_db import client
from gridfs import GridFS

db = client.school
gfs = GridFS(db,collection="book")

file = open("D:/第二讲.pdf","rb")
args = {"type":"PDF","keyword":"课件"}
gfs.put(file,filename="第二讲.pdf",**args)
file.close()