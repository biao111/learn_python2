from datetime import datetime

str_ = '2019-09-10 8:10:56'
str_date = datetime.strptime(str_,'%Y-%m-%d %H:%M:%S')
print(str_date)

now_ = datetime.now()
date_str = now_.strftime('%Y/%m/%d %H:%M:%S')
print(date_str)