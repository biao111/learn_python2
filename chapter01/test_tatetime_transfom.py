from datetime import datetime,date,time,timedelta#timedelta时间加减操作的时间变化量

#自定义时间
d = datetime(2020,10,30,14,5,00)
print(d)


d2 = date(2020,10,15)
print(d2)

t = time(9,0)
print(t)
print("..........")

#日期、时间与字符串之间的转换
#将字符串转换datetime对象
ds = '2018/10/3T13:42:09'
ds_t = datetime.strptime(ds,'%Y/%m/%dT%H:%M:%S')
print(ds_t.second)
print("...........")
#将datetime对象转换为字符串
n = datetime.now()
print(n)
n_str = n.strftime('%m')
print(n_str)

print(".............")
#3.datetime之间的加减操作
n = datetime.now()
print(n)
n_next = n + timedelta(days=5,hours=42)
print(n_next)

print('.............')
#时间减法
d1 = datetime(2018,10,15)
d2 = datetime(2018,11,12)

rest = d2 - d1
print(type(rest))
print(dir(rest))
print(rest.days)