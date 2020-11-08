from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    #操作哈希
    con.hmset("9527",{"name":"scott","sex":"male","age":33})
    con.hset("9527","city","Beijing")
    con.hdel("9527","age")
    result = con.hexists("9527","name")
    print(result)
    result = con.hgetall("9527")
    for one in result:
        print(one.decode("utf-8"),result[one].decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con