import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",port="3306",
#     user="root",password="123456",
#     database="demo"
# )
config={
    "host":"localhost","port":"3306",
    "user":"root","password":"123456",
    "database":"demo"
}
con = mysql.connector.connect(**config)
cursor = con.cursor()
sql="select empno,ename,hiredate from t_emp"
cursor.execute(sql)
for one in cursor:
    print(one[0],one[1],one[2])
con.close()