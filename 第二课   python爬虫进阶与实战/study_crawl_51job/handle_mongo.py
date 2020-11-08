import pymongo


class Mongo_client(object):
    def __init__(self):
        # myclient = pymongo.MongoClient("mongodb://192.168.110.129:27017")
        myclient = pymongo.MongoClient(host='localhost', port=27017)
        myclient.admin.authenticate("admin", "abc123456")
        mydb = myclient['db_51job']
        self.mycollection = mydb['collection_51job']

    def insert_db(self,item):
        self.mycollection.insert_many(item)

insert_data = Mongo_client()
