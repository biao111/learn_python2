from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    #操作列表
    con.delete("dname")
    con.rpush("dname","董事会","秘书部","财务处","技术部")
    con.lpop("dname")
    result = con.lrange("dname","0","-1")
    for one in result:
        print(one.decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con