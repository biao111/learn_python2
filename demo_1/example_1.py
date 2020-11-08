import mysql.connector
con=mysql.connector.connect(
    host="localhost",port="3306",
    user="root",password="123456",
    database="demo"
)

#游标（course） MySQL Connector 利面的游标用来执行SQL语句，而且查询的结果集也保存在游标之中
course = con.cursor()
sql = "SELECT empno,ename,hiredate FROM t_emp;"
course.execute(sql)
for one in course:
    print(one[0],one[1],one[2])

con.close()