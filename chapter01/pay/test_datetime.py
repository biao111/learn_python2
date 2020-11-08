from datetime import  datetime
import time


now_time = datetime.now()
print("now: {0}".format(now_time))
#方法二
print("now：{0}".format(datetime.today()))

#当前的日期
print("now day {0}".format(now_time.date()))

#当前时间
print("now time {0}".format(now_time.time()))

#当前年份
print("year: {0}".format(now_time.year))

#当前月份
print("month {0}".format(now_time.month))

#当前几号
print("day {0}".format(now_time.day))

print(dir(now_time))

print("..............")
print(dir(time))
#获取毫秒数
print(time.time())
#线程
time.sleep(2)