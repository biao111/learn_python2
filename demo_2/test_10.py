from redis_db import pool
import redis
import random
from concurrent.futures import ThreadPoolExecutor

#1.创建一千个随机数
s = set()
while True:
    if len(s) == 1000:
        break
    num = random.randint(1000,10000)
    s.add(num)

#创建连接池
con = redis.Redis(
    connection_pool=pool
)
try:
    #删除已有的数据
    con.delete("kill_num","kill_total","kill_flag","kill_user")
    #创建新的数据
    con.set("kill_num",0)
    con.set("kill_total",50)
    con.set("kill_flag",1)
    con.expire("kill_flag",600)
except Exception as e:
    print(e)
finally:
    del con

#创建进程池大小
executor = ThreadPoolExecutor(10)
#创建被进程池执行的任务
def buy():
    #创建新的连接池
    connection = redis.Redis(
        connection_pool=pool
    )
    pipline = connection.pipeline()
    try:
        if connection.exists("kill_flag") == 1:
            pipline.watch("kill_num","kill_user")
            total = int(pipline.get("kill_total").decode("utf-8"))
            num = int(pipline.get("kill_num").decode("utf-8"))
            if num < total:
                pipline.multi()
                pipline.incr("kill_num")
                user_id = s.pop()
                pipline.rpush("kill_user",user_id)
                pipline.execute()
    except Exception as e:
        print(e)
    finally:
        if "pipline" in dir():
            pipline.reset()
        del connection

#执行进程
for i in range(0,1000):
    executor.submit(buy)

print("秒杀结束！")