import mysql.connector.pooling

confing={
    "host":"localhost","port":3306,
    "user":"root","password":"123456",
    "database":"demo"
}
try:
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **confing,
        pool_size=10
    )
    con=pool.get_connection()
    con.start_transaction()
    cursor= con.cursor()
    sql="UPDATE t_emp SET sal=sal+%s WHERE  deptno=%s"
    cursor.execute(sql,(200,20))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)