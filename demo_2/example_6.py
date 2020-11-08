from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    pipeline = con.pipeline()
    pipeline.watch("9527")
    pipeline.multi()
    pipeline.hset("9527","name","Lihua")
    pipeline.hset("9527","age","23")
    pipeline.execute()
except Exception as e:
    print(e)
finally:
    if "pipeline" in dir():
        pipeline.reset()
    del con