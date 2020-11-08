import mysql.connector
config={
    "host":"localhost","port":3306,
    "user":"root","password":"123456",
    "database":"vega"
}
con=mysql.connector.connect(**config)

#防sql注入攻击，用占位符，不能用字符串连接
username="1 or 1=1"
password="1 or 1=1"
sql="SELECT COUNT(*) FROM t_user WHERE username=%s AND " \
    "AES_DECRYPT(UNHEX(password),'Helloworld')=%s"
cursor = con.cursor()
cursor.execute(sql,(username,password))     #sql,(username,password)先编译sql为二进制，再将参数传进去
print(cursor.fetchone()[0])
con.close()