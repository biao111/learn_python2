from db.redis_db import pool
import redis

class RedisNewsDao():

    #向redis缓存数据
    def insert(self,id,title,username,type,content,is_top,create_time):
       con = redis.Redis(
           connection_pool=pool
       )
       try:
           # con.hset(id,"title",title)
           # con.hset(id, "username", username)
           # con.hset(id, "type", type)
           # con.hset(id, "content", content)
           # con.hset(id, "is_top", is_top)
           # con.hset(id, "create_time", create_time)

           con.hmset(id,{
               "title":title,
               "author":username,
               "type":type,
               "content":content,
               "is_top":is_top,
               "create_time":create_time
           })
           if is_top == 0:
               con.expire(id,24*60*60)
       except Exception as e:
           print(e)
       finally:
           del con

    #删除redis缓存的数据
    def delete_cache(self,id):
        con = redis.Redis(
            connection_pool=pool
        )
        try:
            con.delete(id)
        except Exception as e:
            print(e)
        finally:
            del con